import itertools
import math
from collections import OrderedDict
from collections.abc import Iterable

import cupy as cp
import numpy as np
from cupyx.scipy import ndimage as ndi

from cucim import _misc

from .._shared.utils import check_nD, warn
from ..exposure import histogram
from ..transform import integral_image
from ..util import dtype_limits
from ._sparse import _correlate_sparse, _validate_window_size

__all__ = ['try_all_threshold',
           'threshold_otsu',
           'threshold_yen',
           'threshold_isodata',
           'threshold_li',
           'threshold_local',
           'threshold_minimum',
           'threshold_mean',
           'threshold_niblack',
           'threshold_sauvola',
           'threshold_triangle',
           'apply_hysteresis_threshold',
           'threshold_multiotsu']


def _cumsum(x, *args, **kwargs):
    return cp.cumsum(x, *args, **kwargs)


def _try_all(image, methods=None, figsize=None, num_cols=2, verbose=True):
    """Returns a figure comparing the outputs of different methods.

    Parameters
    ----------
    image : (N, M) ndarray
        Input image.
    methods : dict, optional
        Names and associated functions.
        Functions must take and return an image.
    figsize : tuple, optional
        Figure size (in inches).
    num_cols : int, optional
        Number of columns.
    verbose : bool, optional
        Print function name for each method.

    Returns
    -------
    fig, ax : tuple
        Matplotlib figure and axes.
    """
    from matplotlib import pyplot as plt

    # Handle default value
    methods = methods or {}

    num_rows = math.ceil((len(methods) + 1.0) / num_cols)
    fig, ax = plt.subplots(num_rows, num_cols, figsize=figsize,
                           sharex=True, sharey=True)
    ax = ax.ravel()

    ax[0].imshow(cp.asnumpy(image), cmap=plt.cm.gray)
    ax[0].set_title('Original')

    i = 1
    for name, func in methods.items():
        ax[i].set_title(name)
        try:
            ax[i].imshow(cp.asnumpy(func(image)), cmap=plt.cm.gray)
        except Exception as e:
            ax[i].text(0.5, 0.5, "%s" % type(e).__name__,
                       ha="center", va="center", transform=ax[i].transAxes)
        i += 1
        if verbose:
            print(func.__orifunc__)

    for a in ax:
        a.axis('off')

    fig.tight_layout()
    return fig, ax


def try_all_threshold(image, figsize=(8, 5), verbose=True):
    """Returns a figure comparing the outputs of different thresholding methods.

    Parameters
    ----------
    image : (N, M) ndarray
        Input image.
    figsize : tuple, optional
        Figure size (in inches).
    verbose : bool, optional
        Print function name for each method.

    Returns
    -------
    fig, ax : tuple
        Matplotlib figure and axes.

    Notes
    -----
    The following algorithms are used:

    * isodata
    * li
    * mean
    * minimum
    * otsu
    * triangle
    * yen

    Examples
    --------
    >>> from skimage.data import text
    >>> fig, ax = try_all_threshold(text(), figsize=(10, 6), verbose=False)
    """

    def thresh(func):
        """
        A wrapper function to return a thresholded image.
        """

        def wrapper(im):
            return im > func(im)

        try:
            wrapper.__orifunc__ = func.__orifunc__
        except AttributeError:
            wrapper.__orifunc__ = func.__module__ + "." + func.__name__
        return wrapper

    # Global algorithms.
    methods = OrderedDict({'Isodata': thresh(threshold_isodata),
                           'Li': thresh(threshold_li),
                           'Mean': thresh(threshold_mean),
                           'Minimum': thresh(threshold_minimum),
                           'Otsu': thresh(threshold_otsu),
                           'Triangle': thresh(threshold_triangle),
                           'Yen': thresh(threshold_yen)})

    return _try_all(image, figsize=figsize,
                    methods=methods, verbose=verbose)


def _float_dtype(image):
    if image.dtype.kind == 'f':
        return image.dtype
    return cp.float64


def threshold_local(image, block_size, method='gaussian', offset=0,
                    mode='reflect', param=None, cval=0):
    """Compute a threshold mask image based on local pixel neighborhood.

    Also known as adaptive or dynamic thresholding. The threshold value is
    the weighted mean for the local neighborhood of a pixel subtracted by a
    constant. Alternatively the threshold can be determined dynamically by a
    given function, using the 'generic' method.

    Parameters
    ----------
    image : (N, M) ndarray
        Input image.
    block_size : int
        Odd size of pixel neighborhood which is used to calculate the
        threshold value (e.g. 3, 5, 7, ..., 21, ...).
    method : {'generic', 'gaussian', 'mean', 'median'}, optional
        Method used to determine adaptive threshold for local neighbourhood in
        weighted mean image.

        * 'generic': use custom function (see ``param`` parameter)
        * 'gaussian': apply gaussian filter (see ``param`` parameter for custom\
                      sigma value)
        * 'mean': apply arithmetic mean filter
        * 'median': apply median rank filter

        By default the 'gaussian' method is used.
    offset : float, optional
        Constant subtracted from weighted mean of neighborhood to calculate
        the local threshold value. Default offset is 0.
    mode : {'reflect', 'constant', 'nearest', 'mirror', 'wrap'}, optional
        The mode parameter determines how the array borders are handled, where
        cval is the value when mode is equal to 'constant'.
        Default is 'reflect'.
    param : {int, function}, optional
        Either specify sigma for 'gaussian' method or function object for
        'generic' method. This functions takes the flat array of local
        neighbourhood as a single argument and returns the calculated
        threshold for the centre pixel.
    cval : float, optional
        Value to fill past edges of input if mode is 'constant'.

    Returns
    -------
    threshold : (N, M) ndarray
        Threshold image. All pixels in the input image higher than the
        corresponding pixel in the threshold image are considered foreground.

    References
    ----------
    .. [1] https://docs.opencv.org/modules/imgproc/doc/miscellaneous_transformations.html?highlight=threshold#adaptivethreshold

    Examples
    --------
    >>> from skimage.data import camera
    >>> image = camera()[:50, :50]
    >>> binary_image1 = image > threshold_local(image, 15, 'mean')
    >>> func = lambda arr: arr.mean()
    >>> binary_image2 = image > threshold_local(image, 15, 'generic',
    ...                                         param=func)
    """  # noqa
    if block_size % 2 == 0:
        raise ValueError("The kwarg ``block_size`` must be odd! Given "
                         "``block_size`` {0} is even.".format(block_size))
    check_nD(image, 2)
    thresh_image = cp.zeros(image.shape, _float_dtype(image))
    if method == 'generic':
        raise NotImplementedError("TODO: implement generic_filter")
        ndi.generic_filter(
            image, param, block_size, output=thresh_image, mode=mode, cval=cval
        )
    elif method == 'gaussian':
        if param is None:
            # automatically determine sigma which covers > 99% of distribution
            sigma = (block_size - 1) / 6.0
        else:
            sigma = param
        ndi.gaussian_filter(image, sigma, output=thresh_image, mode=mode,
                            cval=cval)
    elif method == 'mean':
        mask = 1.0 / block_size * cp.ones((block_size,))
        # separation of filters to speedup convolution
        ndi.convolve1d(image, mask, axis=0, output=thresh_image, mode=mode,
                       cval=cval)
        ndi.convolve1d(thresh_image, mask, axis=1, output=thresh_image,
                       mode=mode, cval=cval)
    elif method == 'median':
        ndi.median_filter(image, block_size, output=thresh_image, mode=mode,
                          cval=cval)
    else:
        raise ValueError("Invalid method specified. Please use `generic`, "
                         "`gaussian`, `mean`, or `median`.")

    return thresh_image - offset


def _validate_image_histogram(image, hist, nbins=None):
    """Ensure that either image or hist were given, return valid histogram.

    If hist is given, image is ignored.

    Parameters
    ----------
    image : array or None
        Grayscale image.
    hist : array, 2-tuple of array, or None
        Histogram, either a 1D counts array, or an array of counts together
        with an array of bin centers.
    nbins : int, optional
        The number of bins with which to compute the histogram, if `hist` is
        None.

    Returns
    -------
    counts : 1D array of float
        Each element is the number of pixels falling in each intensity bin.
    bin_centers : 1D array
        Each element is the value corresponding to the center of each intensity
        bin.

    Raises
    ------
    ValueError : if image and hist are both None
    """
    if image is None and hist is None:
        raise Exception("Either image or hist must be provided.")

    if hist is not None:
        if isinstance(hist, (tuple, list)):
            counts, bin_centers = hist
        else:
            counts = hist
            bin_centers = cp.arange(counts.size)
    else:
        counts, bin_centers = histogram(
            image.ravel(), nbins, source_range="image"
        )
    return counts.astype(float), bin_centers


def threshold_otsu(image=None, nbins=256, *, hist=None):
    """Return threshold value based on Otsu's method.

    Either image or hist must be provided. If hist is provided, the actual
    histogram of the image is ignored.

    Parameters
    ----------
    image : (N, M) ndarray, optional
        Grayscale input image.
    nbins : int, optional
        Number of bins used to calculate histogram. This value is ignored for
        integer arrays.
    hist : array, or 2-tuple of arrays, optional
        Histogram from which to determine the threshold, and optionally a
        corresponding array of bin center intensities.
        An alternative use of this function is to pass it only hist.

    Returns
    -------
    threshold : float
        Upper threshold value. All pixels with an intensity higher than
        this value are assumed to be foreground.

    References
    ----------
    .. [1] Wikipedia, https://en.wikipedia.org/wiki/Otsu's_Method

    Examples
    --------
    >>> from skimage.data import camera
    >>> image = camera()
    >>> thresh = threshold_otsu(image)
    >>> binary = image <= thresh

    Notes
    -----
    The input image must be grayscale.
    """
    if image is not None and image.ndim > 2 and image.shape[-1] in (3, 4):
        msg = "threshold_otsu is expected to work correctly only for " \
              "grayscale images; image shape {0} looks like an RGB image"
        warn(msg.format(image.shape))

    # Check if the image is multi-colored or not
    # Check if the image has more than one intensity value; if not, return that
    # value
    if image is not None:
        first_pixel = image.ravel()[0]
        if cp.all(image == first_pixel):  # device synchronization!
            return first_pixel

    counts, bin_centers = _validate_image_histogram(image, hist, nbins)

    # class probabilities for all possible thresholds
    weight1 = _cumsum(counts)
    weight2 = _cumsum(counts[::-1])[::-1]
    # class means for all possible thresholds
    mean1 = _cumsum(counts * bin_centers) / weight1
    mean2 = (_cumsum((counts * bin_centers)[::-1]) / weight2[::-1])[::-1]

    # Clip ends to align class 1 and class 2 variables:
    # The last value of ``weight1``/``mean1`` should pair with zero values in
    # ``weight2``/``mean2``, which do not exist.
    variance12 = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2

    idx = cp.argmax(variance12)
    threshold = bin_centers[idx]

    return threshold


def threshold_yen(image=None, nbins=256, *, hist=None):
    """Return threshold value based on Yen's method.
    Either image or hist must be provided. In case hist is given, the actual
    histogram of the image is ignored.

    Parameters
    ----------
    image : (N, M) ndarray, optional
        Input image.
    nbins : int, optional
        Number of bins used to calculate histogram. This value is ignored for
        integer arrays.
    hist : array, or 2-tuple of arrays, optional
        Histogram from which to determine the threshold, and optionally a
        corresponding array of bin center intensities.
        An alternative use of this function is to pass it only hist.

    Returns
    -------
    threshold : float
        Upper threshold value. All pixels with an intensity higher than
        this value are assumed to be foreground.

    References
    ----------
    .. [1] Yen J.C., Chang F.J., and Chang S. (1995) "A New Criterion
           for Automatic Multilevel Thresholding" IEEE Trans. on Image
           Processing, 4(3): 370-378. :DOI:`10.1109/83.366472`
    .. [2] Sezgin M. and Sankur B. (2004) "Survey over Image Thresholding
           Techniques and Quantitative Performance Evaluation" Journal of
           Electronic Imaging, 13(1): 146-165, :DOI:`10.1117/1.1631315`
           http://www.busim.ee.boun.edu.tr/~sankur/SankurFolder/Threshold_survey.pdf
    .. [3] ImageJ AutoThresholder code, http://fiji.sc/wiki/index.php/Auto_Threshold

    Examples
    --------
    >>> from skimage.data import camera
    >>> image = camera()
    >>> thresh = threshold_yen(image)
    >>> binary = image <= thresh
    """  # noqa
    counts, bin_centers = _validate_image_histogram(image, hist, nbins)

    # On blank images (e.g. filled with 0) with int dtype, `histogram()`
    # returns ``bin_centers`` containing only one value. Speed up with it.
    if bin_centers.size == 1:
        return bin_centers[0]

    # Calculate probability mass function
    pmf = counts.astype(cp.float32) / counts.sum()
    P1 = _cumsum(pmf)  # Cumulative normalized histogram
    P1_sq = _cumsum(pmf * pmf)
    # Get cumsum calculated from end of squared array:
    P2_sq = _cumsum(pmf[::-1] ** 2)[::-1]
    # P2_sq indexes is shifted +1. I assume, with P1[:-1] it's help avoid
    # '-inf' in crit. ImageJ Yen implementation replaces those values by zero.
    crit = cp.log(((P1_sq[:-1] * P2_sq[1:]) ** -1) *
                  (P1[:-1] * (1.0 - P1[:-1])) ** 2)
    return bin_centers[crit.argmax()]


def threshold_isodata(image=None, nbins=256, return_all=False, *, hist=None):
    """Return threshold value(s) based on ISODATA method.

    Histogram-based threshold, known as Ridler-Calvard method or inter-means.
    Threshold values returned satisfy the following equality::

        threshold = (image[image <= threshold].mean() +
                     image[image > threshold].mean()) / 2.0

    That is, returned thresholds are intensities that separate the image into
    two groups of pixels, where the threshold intensity is midway between the
    mean intensities of these groups.

    For integer images, the above equality holds to within one; for floating-
    point images, the equality holds to within the histogram bin-width.

    Either image or hist must be provided. In case hist is given, the actual
    histogram of the image is ignored.

    Parameters
    ----------
    image : (N, M) ndarray, optional
        Input image.
    nbins : int, optional
        Number of bins used to calculate histogram. This value is ignored for
        integer arrays.
    return_all : bool, optional
        If False (default), return only the lowest threshold that satisfies
        the above equality. If True, return all valid thresholds.
    hist : array, or 2-tuple of arrays, optional
        Histogram to determine the threshold from and a corresponding array
        of bin center intensities. Alternatively, only the histogram can be
        passed.

    Returns
    -------
    threshold : float or int or array
        Threshold value(s).

    References
    ----------
    .. [1] Ridler, TW & Calvard, S (1978), "Picture thresholding using an
           iterative selection method"
           IEEE Transactions on Systems, Man and Cybernetics 8: 630-632,
           :DOI:`10.1109/TSMC.1978.4310039`
    .. [2] Sezgin M. and Sankur B. (2004) "Survey over Image Thresholding
           Techniques and Quantitative Performance Evaluation" Journal of
           Electronic Imaging, 13(1): 146-165,
           http://www.busim.ee.boun.edu.tr/~sankur/SankurFolder/Threshold_survey.pdf
           :DOI:`10.1117/1.1631315`
    .. [3] ImageJ AutoThresholder code,
           http://fiji.sc/wiki/index.php/Auto_Threshold

    Examples
    --------
    >>> from skimage.data import coins
    >>> image = coins()
    >>> thresh = threshold_isodata(image)
    >>> binary = image > thresh
    """
    counts, bin_centers = _validate_image_histogram(image, hist, nbins)

    # image only contains one unique value
    if len(bin_centers) == 1:
        if return_all:
            return bin_centers
        else:
            return bin_centers[0]

    counts = counts.astype(cp.float32)

    # csuml and csumh contain the count of pixels in that bin or lower, and
    # in all bins strictly higher than that bin, respectively
    csuml = _cumsum(counts)
    csumh = csuml[-1] - csuml

    # intensity_sum contains the total pixel intensity from each bin
    intensity_sum = counts * bin_centers

    # l and h contain average value of all pixels in that bin or lower, and
    # in all bins strictly higher than that bin, respectively.
    # Note that since exp.histogram does not include empty bins at the low or
    # high end of the range, csuml and csumh are strictly > 0, except in the
    # last bin of csumh, which is zero by construction.
    # So no worries about division by zero in the following lines, except
    # for the last bin, but we can ignore that because no valid threshold
    # can be in the top bin.
    # To avoid the division by zero, we simply skip over the last element in
    # all future computation.
    csum_intensity = _cumsum(intensity_sum)
    lower = csum_intensity[:-1] / csuml[:-1]
    higher = (csum_intensity[-1] - csum_intensity[:-1]) / csumh[:-1]

    # isodata finds threshold values that meet the criterion t = (l + m)/2
    # where l is the mean of all pixels <= t and h is the mean of all pixels
    # > t, as calculated above. So we are looking for places where
    # (l + m) / 2 equals the intensity value for which those l and m figures
    # were calculated -- which is, of course, the histogram bin centers.
    # We only require this equality to be within the precision of the bin
    # width, of course.
    all_mean = (lower + higher) / 2.0
    bin_width = bin_centers[1] - bin_centers[0]

    # Look only at thresholds that are below the actual all_mean value,
    # for consistency with the threshold being included in the lower pixel
    # group. Otherwise can get thresholds that are not actually fixed-points
    # of the isodata algorithm. For float images, this matters less, since
    # there really can't be any guarantees anymore anyway.
    distances = all_mean - bin_centers[:-1]
    thresholds = bin_centers[:-1][(distances >= 0) & (distances < bin_width)]

    if return_all:
        return thresholds
    else:
        return thresholds[0]


# Computing a histogram using cp.histogram on a uint8 image with bins=256
# doesn't work and results in aliasing problems. We use a fully specified set
# of bins to ensure that each uint8 value false into its own bin.
_DEFAULT_ENTROPY_BINS = tuple(np.arange(-0.5, 255.51, 1))


def _cross_entropy(image, threshold, bins=_DEFAULT_ENTROPY_BINS):
    """Compute cross-entropy between distributions above and below a threshold.

    Parameters
    ----------
    image : array
        The input array of values.
    threshold : float
        The value dividing the foreground and background in ``image``.
    bins : int or array of float, optional
        The number of bins or the bin edges. (Any valid value to the ``bins``
        argument of ``cp.histogram`` will work here.) For an exact calculation,
        each unique value should have its own bin. The default value for bins
        ensures exact handling of uint8 images: ``bins=256`` results in
        aliasing problems due to bin width not being equal to 1.

    Returns
    -------
    nu : float
        The cross-entropy target value as defined in [1]_.

    Notes
    -----
    See Li and Lee, 1993 [1]_; this is the objective function ``threshold_li``
    minimizes. This function can be improved but this implementation most
    closely matches equation 8 in [1]_ and equations 1-3 in [2]_.

    References
    ----------
    .. [1] Li C.H. and Lee C.K. (1993) "Minimum Cross Entropy Thresholding"
           Pattern Recognition, 26(4): 617-625
           :DOI:`10.1016/0031-3203(93)90115-D`
    .. [2] Li C.H. and Tam P.K.S. (1998) "An Iterative Algorithm for Minimum
           Cross Entropy Thresholding" Pattern Recognition Letters, 18(8): 771-776
           :DOI:`10.1016/S0167-8655(98)00057-9`
    """  # noqa
    bins = cp.asarray(bins)  # required for _DEFAULT_ENTROPY_BINS tuple
    histogram, bin_edges = cp.histogram(image, bins=bins, density=True)
    bin_centers = cp.convolve(bin_edges, cp.array([0.5, 0.5]), mode='valid')
    t = cp.flatnonzero(bin_centers > threshold)[0]
    m0a = cp.sum(histogram[:t])  # 0th moment, background
    m0b = cp.sum(histogram[t:])
    m1a = cp.sum(histogram[:t] * bin_centers[:t])  # 1st moment, background
    m1b = cp.sum(histogram[t:] * bin_centers[t:])
    mua = m1a / m0a  # mean value, background
    mub = m1b / m0b
    nu = -m1a * cp.log(mua) - m1b * cp.log(mub)
    return nu


def threshold_li(image, *, tolerance=None, initial_guess=None,
                 iter_callback=None):
    """Compute threshold value by Li's iterative Minimum Cross Entropy method.

    Parameters
    ----------
    image : ndarray
        Input image.

    tolerance : float, optional
        Finish the computation when the change in the threshold in an iteration
        is less than this value. By default, this is half the smallest
        difference between intensity values in ``image``.

    initial_guess : float or Callable[[array[float]], float], optional
        Li's iterative method uses gradient descent to find the optimal
        threshold. If the image intensity histogram contains more than two
        modes (peaks), the gradient descent could get stuck in a local optimum.
        An initial guess for the iteration can help the algorithm find the
        globally-optimal threshold. A float value defines a specific start
        point, while a callable should take in an array of image intensities
        and return a float value. Example valid callables include
        ``numpy.mean`` (default), ``lambda arr: numpy.quantile(arr, 0.95)``,
        or even :func:`skimage.filters.threshold_otsu`.

    iter_callback : Callable[[float], Any], optional
        A function that will be called on the threshold at every iteration of
        the algorithm.

    Returns
    -------
    threshold : float
        Upper threshold value. All pixels with an intensity higher than
        this value are assumed to be foreground.

    References
    ----------
    .. [1] Li C.H. and Lee C.K. (1993) "Minimum Cross Entropy Thresholding"
           Pattern Recognition, 26(4): 617-625
           :DOI:`10.1016/0031-3203(93)90115-D`
    .. [2] Li C.H. and Tam P.K.S. (1998) "An Iterative Algorithm for Minimum
           Cross Entropy Thresholding" Pattern Recognition Letters, 18(8): 771-776
           :DOI:`10.1016/S0167-8655(98)00057-9`
    .. [3] Sezgin M. and Sankur B. (2004) "Survey over Image Thresholding
           Techniques and Quantitative Performance Evaluation" Journal of
           Electronic Imaging, 13(1): 146-165
           :DOI:`10.1117/1.1631315`
    .. [4] ImageJ AutoThresholder code, http://fiji.sc/wiki/index.php/Auto_Threshold

    Examples
    --------
    >>> from skimage.data import camera
    >>> image = camera()
    >>> thresh = threshold_li(image)
    >>> binary = image > thresh
    """  # noqa
    # Remove nan:
    image = image[~cp.isnan(image)]
    if image.size == 0:
        return cp.nan

    # Make sure image has more than one value; otherwise, return that value
    # This works even for cp.inf
    val0 = image.ravel()[0]
    if cp.all(image == val0):  # device synchronize!
        return val0

    # At this point, the image only contains cp.inf, -cp.inf, or valid numbers
    image = image[cp.isfinite(image)]
    # if there are no finite values in the image, return 0. This is because
    # at this point we *know* that there are *both* inf and -inf values,
    # because inf == inf evaluates to True. We might as well separate them.
    if image.size == 0:
        return 0.0

    # Li's algorithm requires positive image (because of log(mean))
    image_min = cp.min(image)
    image -= image_min
    tolerance = tolerance or cp.min(cp.diff(cp.unique(image))) / 2

    # Initial estimate for iteration. See "initial_guess" in the parameter list
    if initial_guess is None:
        t_next = cp.mean(image)
    elif callable(initial_guess):
        t_next = initial_guess(image)
    elif cp.isscalar(initial_guess):  # convert to new, positive image range
        t_next = initial_guess - image_min
        image_max = cp.max(image) + image_min
        if not 0 < t_next < cp.max(image):
            msg = ('The initial guess for threshold_li must be within the '
                   'range of the image. Got {} for image min {} and max {} '
                   .format(initial_guess, image_min, image_max))
            raise ValueError(msg)
    else:
        raise TypeError('Incorrect type for `initial_guess`; should be '
                        'a floating point value, or a function mapping an '
                        'array to a floating point value.')

    # initial value for t_curr must be different from t_next by at
    # least the tolerance. Since the image is positive, we ensure this
    # by setting to a large-enough negative number
    t_curr = -2 * tolerance

    # Callback on initial iterations
    if iter_callback is not None:
        iter_callback(t_next + image_min)

    # Stop the iterations when the difference between the
    # new and old threshold values is less than the tolerance
    while abs(t_next - t_curr) > tolerance:
        t_curr = t_next
        foreground = image > t_curr
        mean_fore = cp.mean(image[foreground])
        mean_back = cp.mean(image[~foreground])

        t_next = ((mean_back - mean_fore) /
                  (cp.log(mean_back) - cp.log(mean_fore)))

        if iter_callback is not None:
            iter_callback(t_next + image_min)

    threshold = t_next + image_min
    return threshold


def threshold_minimum(image=None, nbins=256, max_iter=10000, *, hist=None):
    """Return threshold value based on minimum method.

    The histogram of the input ``image`` is computed if not provided and
    smoothed until there are only two maxima. Then the minimum in between is
    the threshold value.

    Either image or hist must be provided. In case hist is given, the actual
    histogram of the image is ignored.

    Parameters
    ----------
    image : (M, N) ndarray, optional
        Input image.
    nbins : int, optional
        Number of bins used to calculate histogram. This value is ignored for
        integer arrays.
    max_iter : int, optional
        Maximum number of iterations to smooth the histogram.
    hist : array, or 2-tuple of arrays, optional
        Histogram to determine the threshold from and a corresponding array
        of bin center intensities. Alternatively, only the histogram can be
        passed.

    Returns
    -------
    threshold : float
        Upper threshold value. All pixels with an intensity higher than
        this value are assumed to be foreground.

    Raises
    ------
    RuntimeError
        If unable to find two local maxima in the histogram or if the
        smoothing takes more than 1e4 iterations.

    References
    ----------
    .. [1] C. A. Glasbey, "An analysis of histogram-based thresholding
           algorithms," CVGIP: Graphical Models and Image Processing,
           vol. 55, pp. 532-537, 1993.
    .. [2] Prewitt, JMS & Mendelsohn, ML (1966), "The analysis of cell
           images", Annals of the New York Academy of Sciences 128: 1035-1053
           :DOI:`10.1111/j.1749-6632.1965.tb11715.x`

    Examples
    --------
    >>> from skimage.data import camera
    >>> image = camera()
    >>> thresh = threshold_minimum(image)
    >>> binary = image > thresh
    """

    def find_local_maxima_idx(hist):
        # We can't use scipy.signal.argrelmax
        # as it fails on plateaus
        maximum_idxs = list()
        direction = 1

        # TODO: better to transfer hist back to cpu?
        hist = cp.asnumpy(hist)  # device synchronize

        for i in range(hist.shape[0] - 1):
            if direction > 0:
                if hist[i + 1] < hist[i]:
                    direction = -1
                    maximum_idxs.append(i)
            else:
                if hist[i + 1] > hist[i]:
                    direction = 1

        return maximum_idxs

    counts, bin_centers = _validate_image_histogram(image, hist, nbins)

    smooth_hist = counts.astype(cp.float64, copy=False)

    for counter in range(max_iter):
        smooth_hist = ndi.uniform_filter1d(smooth_hist, 3)
        maximum_idxs = find_local_maxima_idx(smooth_hist)
        if len(maximum_idxs) < 3:
            break

    if len(maximum_idxs) != 2:
        raise RuntimeError('Unable to find two maxima in histogram')
    elif counter == max_iter - 1:
        raise RuntimeError('Maximum iteration reached for histogram'
                           'smoothing')

    # Find lowest point between the maxima
    threshold_idx = cp.argmin(
        smooth_hist[maximum_idxs[0]:maximum_idxs[1] + 1]
    )

    return bin_centers[maximum_idxs[0] + int(threshold_idx)]


def threshold_mean(image):
    """Return threshold value based on the mean of grayscale values.

    Parameters
    ----------
    image : (N, M[, ..., P]) ndarray
        Grayscale input image.

    Returns
    -------
    threshold : float
        Upper threshold value. All pixels with an intensity higher than
        this value are assumed to be foreground.

    References
    ----------
    .. [1] C. A. Glasbey, "An analysis of histogram-based thresholding
        algorithms," CVGIP: Graphical Models and Image Processing,
        vol. 55, pp. 532-537, 1993.
        :DOI:`10.1006/cgip.1993.1040`

    Examples
    --------
    >>> from skimage.data import camera
    >>> image = camera()
    >>> thresh = threshold_mean(image)
    >>> binary = image > thresh
    """
    return cp.mean(image)


def threshold_triangle(image, nbins=256):
    """Return threshold value based on the triangle algorithm.

    Parameters
    ----------
    image : (N, M[, ..., P]) ndarray
        Grayscale input image.
    nbins : int, optional
        Number of bins used to calculate histogram. This value is ignored for
        integer arrays.

    Returns
    -------
    threshold : float
        Upper threshold value. All pixels with an intensity higher than
        this value are assumed to be foreground.

    References
    ----------
    .. [1] Zack, G. W., Rogers, W. E. and Latt, S. A., 1977,
       Automatic Measurement of Sister Chromatid Exchange Frequency,
       Journal of Histochemistry and Cytochemistry 25 (7), pp. 741-753
       :DOI:`10.1177/25.7.70454`
    .. [2] ImageJ AutoThresholder code,
       http://fiji.sc/wiki/index.php/Auto_Threshold

    Examples
    --------
    >>> from skimage.data import camera
    >>> image = camera()
    >>> thresh = threshold_triangle(image)
    >>> binary = image > thresh
    """
    # nbins is ignored for integer arrays
    # so, we recalculate the effective nbins.
    hist, bin_centers = histogram(image.ravel(), nbins, source_range='image')
    nbins = len(hist)

    # Find peak, lowest and highest gray levels.
    arg_peak_height = cp.argmax(hist)
    peak_height = hist[arg_peak_height]
    arg_low_level, arg_high_level = cp.where(hist > 0)[0][[0, -1]]

    # Flip is True if left tail is shorter.
    flip = arg_peak_height - arg_low_level < arg_high_level - arg_peak_height
    if flip:
        hist = hist[::-1]
        arg_low_level = nbins - arg_high_level - 1
        arg_peak_height = nbins - arg_peak_height - 1

    # If flip == True, arg_high_level becomes incorrect
    # but we don't need it anymore.
    del arg_high_level

    # Set up the coordinate system.
    width = arg_peak_height - arg_low_level
    x1 = cp.arange(width)
    y1 = hist[x1 + arg_low_level]

    # Normalize.
    norm = cp.sqrt(peak_height ** 2 + width ** 2)
    try:
        peak_height /= norm
        width /= norm
    except TypeError:
        # TODO: CuPy bug?
        # workaround for:
        #    TypeError: output (typecode 'd') could not be coerced to provided
        #    output parameter (typecode 'l') according to the casting rule
        #    "same_kind"
        peak_height = peak_height / norm
        width = width / norm

    # Maximize the length.
    # The ImageJ implementation includes an additional constant when calculating
    # the length, but here we omit it as it does not affect the location of the
    # minimum.
    length = peak_height * x1 - width * y1
    arg_level = cp.argmax(length) + arg_low_level

    if flip:
        arg_level = nbins - arg_level - 1

    return bin_centers[arg_level]


def _mean_std(image, w):
    """Return local mean and standard deviation of each pixel using a
    neighborhood defined by a rectangular window size ``w``.
    The algorithm uses integral images to speedup computation. This is
    used by :func:`threshold_niblack` and :func:`threshold_sauvola`.

    Parameters
    ----------
    image : ndarray
        Input image.
    w : int, or iterable of int
        Window size specified as a single odd integer (3, 5, 7, …),
        or an iterable of length ``image.ndim`` containing only odd
        integers (e.g. ``(1, 5, 5)``).

    Returns
    -------
    m : ndarray of float, same shape as ``image``
        Local mean of the image.
    s : ndarray of float, same shape as ``image``
        Local standard deviation of the image.

    References
    ----------
    .. [1] F. Shafait, D. Keysers, and T. M. Breuel, "Efficient
           implementation of local adaptive thresholding techniques
           using integral images." in Document Recognition and
           Retrieval XV, (San Jose, USA), Jan. 2008.
           :DOI:`10.1117/12.767755`
    """
    if not isinstance(w, Iterable):
        w = (w,) * image.ndim
    _validate_window_size(w)

    pad_width = tuple((k // 2 + 1, k // 2) for k in w)
    padded = cp.pad(image.astype('float'), pad_width,
                    mode='reflect')

    integral = integral_image(padded)
    padded *= padded
    integral_sq = integral_image(padded)

    # Store the kernel as a list 2-tuples where:
    #     - The first element is an index into the kernel (of shape w).
    #     - The second element is the value at that index.
    kernel_indices_and_values = []
    for indices in itertools.product(*tuple([(0, _w) for _w in w])):
        kernel_indices_and_values.append(
            (indices, (-1) ** (image.ndim % 2 != np.sum(indices) % 2))
        )

    total_window_size = _misc.prod(w)
    kernel_shape = tuple(_w + 1 for _w in w)
    m = _correlate_sparse(integral, kernel_shape, kernel_indices_and_values)
    m /= total_window_size
    g2 = _correlate_sparse(integral_sq, kernel_shape,
                           kernel_indices_and_values)
    g2 /= total_window_size
    # Note: we use np.clip because g2 is not guaranteed to be greater than
    # m*m when floating point error is considered
    s = cp.clip(g2 - m * m, 0, None)
    cp.sqrt(s, out=s)
    return m, s


def threshold_niblack(image, window_size=15, k=0.2):
    """Applies Niblack local threshold to an array.

    A threshold T is calculated for every pixel in the image using the
    following formula::

        T = m(x,y) - k * s(x,y)

    where m(x,y) and s(x,y) are the mean and standard deviation of
    pixel (x,y) neighborhood defined by a rectangular window with size w
    times w centered around the pixel. k is a configurable parameter
    that weights the effect of standard deviation.

    Parameters
    ----------
    image : ndarray
        Input image.
    window_size : int, or iterable of int, optional
        Window size specified as a single odd integer (3, 5, 7, …),
        or an iterable of length ``image.ndim`` containing only odd
        integers (e.g. ``(1, 5, 5)``).
    k : float, optional
        Value of parameter k in threshold formula.

    Returns
    -------
    threshold : (N, M) ndarray
        Threshold mask. All pixels with an intensity higher than
        this value are assumed to be foreground.

    Notes
    -----
    This algorithm is originally designed for text recognition.

    The Bradley threshold is a particular case of the Niblack
    one, being equivalent to

    >>> from skimage import data
    >>> image = data.page()
    >>> q = 1
    >>> threshold_image = threshold_niblack(image, k=0) * q

    for some value ``q``. By default, Bradley and Roth use ``q=1``.


    References
    ----------
    .. [1] W. Niblack, An introduction to Digital Image Processing,
           Prentice-Hall, 1986.
    .. [2] D. Bradley and G. Roth, "Adaptive thresholding using Integral
           Image", Journal of Graphics Tools 12(2), pp. 13-21, 2007.
           :DOI:`10.1080/2151237X.2007.10129236`

    Examples
    --------
    >>> from skimage import data
    >>> image = data.page()
    >>> threshold_image = threshold_niblack(image, window_size=7, k=0.1)
    """
    m, s = _mean_std(image, window_size)
    return m - k * s


def threshold_sauvola(image, window_size=15, k=0.2, r=None):
    """Applies Sauvola local threshold to an array. Sauvola is a
    modification of Niblack technique.

    In the original method a threshold T is calculated for every pixel
    in the image using the following formula::

        T = m(x,y) * (1 + k * ((s(x,y) / R) - 1))

    where m(x,y) and s(x,y) are the mean and standard deviation of
    pixel (x,y) neighborhood defined by a rectangular window with size w
    times w centered around the pixel. k is a configurable parameter
    that weights the effect of standard deviation.
    R is the maximum standard deviation of a greyscale image.

    Parameters
    ----------
    image : ndarray
        Input image.
    window_size : int, or iterable of int, optional
        Window size specified as a single odd integer (3, 5, 7, …),
        or an iterable of length ``image.ndim`` containing only odd
        integers (e.g. ``(1, 5, 5)``).
    k : float, optional
        Value of the positive parameter k.
    r : float, optional
        Value of R, the dynamic range of standard deviation.
        If None, set to the half of the image dtype range.

    Returns
    -------
    threshold : (N, M) ndarray
        Threshold mask. All pixels with an intensity higher than
        this value are assumed to be foreground.

    Notes
    -----
    This algorithm is originally designed for text recognition.

    References
    ----------
    .. [1] J. Sauvola and M. Pietikainen, "Adaptive document image
           binarization," Pattern Recognition 33(2),
           pp. 225-236, 2000.
           :DOI:`10.1016/S0031-3203(99)00055-2`

    Examples
    --------
    >>> from skimage import data
    >>> image = data.page()
    >>> t_sauvola = threshold_sauvola(image, window_size=15, k=0.2)
    >>> binary_image = image > t_sauvola
    """
    if r is None:
        imin, imax = dtype_limits(image, clip_negative=False)
        r = 0.5 * (imax - imin)
    m, s = _mean_std(image, window_size)
    return m * (1 + k * ((s / r) - 1))


def apply_hysteresis_threshold(image, low, high):
    """Apply hysteresis thresholding to ``image``.

    This algorithm finds regions where ``image`` is greater than ``high``
    OR ``image`` is greater than ``low`` *and* that region is connected to
    a region greater than ``high``.

    Parameters
    ----------
    image : array, shape (M,[ N, ..., P])
        Grayscale input image.
    low : float, or array of same shape as ``image``
        Lower threshold.
    high : float, or array of same shape as ``image``
        Higher threshold.

    Returns
    -------
    thresholded : array of bool, same shape as ``image``
        Array in which ``True`` indicates the locations where ``image``
        was above the hysteresis threshold.

    Examples
    --------
    >>> import cupy as cp
    >>> from cucim.skimage.filters import apply_hysteresis_threshold
    >>> image = cp.asarray([1, 2, 3, 2, 1, 2, 1, 3, 2])
    >>> apply_hysteresis_threshold(image, 1.5, 2.5).astype(int)
    array([0, 1, 1, 1, 0, 0, 0, 1, 1])

    References
    ----------
    .. [1] J. Canny. A computational approach to edge detection.
           IEEE Transactions on Pattern Analysis and Machine Intelligence.
           1986; vol. 8, pp.679-698.
           :DOI:`10.1109/TPAMI.1986.4767851`
    """
    low = cp.asarray(low)  # asarray to allow scalar low
    # ensure low always below high
    low = cp.clip(low, a_min=None, a_max=high)
    mask_low = image > low
    mask_high = image > high
    # Connected components of mask_low
    labels_low, num_labels = ndi.label(mask_low)
    # Check which connected components contain pixels from mask_high

    # CuPy Backend: refactored in the same style as features.canny to avoid
    #               slow call to cupyx.scipy.ndimage.sum
    nonzero_sums = cp.unique(labels_low[mask_high])
    connected_to_high = cp.zeros((num_labels + 1,), bool)
    connected_to_high[nonzero_sums] = True
    thresholded = connected_to_high[labels_low]
    return thresholded


def threshold_multiotsu(image, classes=3, nbins=256):
    r"""Generate `classes`-1 threshold values to divide gray levels in `image`.

    The threshold values are chosen to maximize the total sum of pairwise
    variances between the thresholded graylevel classes. See Notes and [1]_
    for more details.

    Parameters
    ----------
    image : (N, M) ndarray
        Grayscale input image.
    classes : int, optional
        Number of classes to be thresholded, i.e. the number of resulting
        regions.
    nbins : int, optional
        Number of bins used to calculate the histogram. This value is ignored
        for integer arrays.

    Returns
    -------
    thresh : array
        Array containing the threshold values for the desired classes.

    Raises
    ------
    ValueError
         If ``image`` contains less grayscale value then the desired
         number of classes.

    Notes
    -----
    This implementation relies on a Cython function whose complexity
    is :math:`O\left(\frac{Ch^{C-1}}{(C-1)!}\right)`, where :math:`h`
    is the number of histogram bins and :math:`C` is the number of
    classes desired.

    The input image must be grayscale.

    References
    ----------
    .. [1] Liao, P-S., Chen, T-S. and Chung, P-C., "A fast algorithm for
           multilevel thresholding", Journal of Information Science and
           Engineering 17 (5): 713-727, 2001. Available at:
           <https://ftp.iis.sinica.edu.tw/JISE/2001/200109_01.pdf>
           :DOI:`10.6688/JISE.2001.17.5.1`
    .. [2] Tosa, Y., "Multi-Otsu Threshold", a java plugin for ImageJ.
           Available at:
           <http://imagej.net/plugins/download/Multi_OtsuThreshold.java>

    Examples
    --------
    >>> import cupy as cp
    >>> from cucim.skimage.color import label2rgb
    >>> from skimage import data
    >>> image = cp.asarray(data.camera())
    >>> thresholds = threshold_multiotsu(image)
    >>> regions = cp.digitize(image, bins=thresholds)
    >>> regions_colorized = label2rgb(regions)

    """
    try:
        from skimage.filters._multiotsu import (
            _get_multiotsu_thresh_indices, _get_multiotsu_thresh_indices_lut)
    except ImportError:
        raise ImportError(
            "could not the required (private) multi-otsu helper functions "
            "from scikit-image"
        )

    if len(image.shape) > 2 and image.shape[-1] in (3, 4):
        msg = ("threshold_multiotsu is expected to work correctly only for "
               "grayscale images; image shape {0} looks like an RGB image")
        warn(msg.format(image.shape))

    # calculating the histogram and the probability of each gray level.
    prob, bin_centers = histogram(image.ravel(),
                                  nbins=nbins,
                                  source_range='image',
                                  normalize=True)

    nvalues = cp.count_nonzero(prob)
    if nvalues < classes:
        msg = ("The input image has only {} different values. "
               "It can not be thresholded in {} classes")
        raise ValueError(msg.format(nvalues, classes))
    elif nvalues == classes:
        thresh_idx = cp.where(prob > 0)[0][:-1]
    else:
        # Need probabilities on the CPU to use the Cython code
        # CuPy Backend: prob is small, so CPU computations should be faster
        prob = cp.asnumpy(prob)  # synchronization!
        prob = prob.astype("float32")

        # Get threshold indices
        try:
            thresh_idx = _get_multiotsu_thresh_indices_lut(prob, classes - 1)
        except MemoryError:
            # Don't use LUT if the number of bins is too large (if the
            # image is uint16 for example): in this case, the
            # allocated memory is too large.
            thresh_idx = _get_multiotsu_thresh_indices(prob, classes - 1)
        # transfer indices back to the GPU
        thresh_idx = cp.asarray(thresh_idx)  # synchronization!

    thresh = bin_centers[thresh_idx]

    return thresh
