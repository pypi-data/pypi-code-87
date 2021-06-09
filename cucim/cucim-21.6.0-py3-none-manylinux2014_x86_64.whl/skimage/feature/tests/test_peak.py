import itertools
import unittest

import cupy as cp
import numpy as np
import pytest
from cupy.testing import assert_array_almost_equal, assert_array_equal
from cupyx.scipy import ndimage as ndi
from scipy import ndimage as ndimage_cpu

from cucim.skimage._shared._warnings import expected_warnings
from cucim.skimage.feature import peak

np.random.seed(21)


class TestPeakLocalMax:
    def test_trivial_case(self):
        trivial = cp.zeros((25, 25))
        peak_indices = peak.peak_local_max(trivial, min_distance=1)
        assert type(peak_indices) is cp.ndarray
        assert peak_indices.size == 0
        with expected_warnings(["indices argument is deprecated"]):
            peaks = peak.peak_local_max(trivial, min_distance=1,
                                        indices=False)
        assert (peaks.astype(bool) == trivial).all()

    def test_noisy_peaks(self):
        peak_locations = [(7, 7), (7, 13), (13, 7), (13, 13)]

        # image with noise of amplitude 0.8 and peaks of amplitude 1
        image = 0.8 * cp.asarray(np.random.rand(20, 20))
        for r, c in peak_locations:
            image[r, c] = 1

        peaks_detected = peak.peak_local_max(image, min_distance=5)

        assert len(peaks_detected) == len(peak_locations)
        for loc in peaks_detected:
            assert tuple(loc) in peak_locations

    def test_relative_threshold(self):
        image = cp.zeros((5, 5), dtype=cp.uint8)
        image[1, 1] = 10
        image[3, 3] = 20
        peaks = peak.peak_local_max(image, min_distance=1, threshold_rel=0.5)
        assert len(peaks) == 1
        assert_array_almost_equal(peaks, [(3, 3)])

    def test_absolute_threshold(self):
        image = cp.zeros((5, 5), dtype=cp.uint8)
        image[1, 1] = 10
        image[3, 3] = 20
        peaks = peak.peak_local_max(image, min_distance=1, threshold_abs=10)
        assert len(peaks) == 1
        assert_array_almost_equal(peaks, [(3, 3)])

    def test_constant_image(self):
        image = cp.full((20, 20), 128, dtype=cp.uint8)
        peaks = peak.peak_local_max(image, min_distance=1)
        assert len(peaks) == 0

    def test_flat_peak(self):
        image = cp.zeros((5, 5), dtype=cp.uint8)
        image[1:3, 1:3] = 10
        peaks = peak.peak_local_max(image, min_distance=1)
        assert len(peaks) == 4

    def test_sorted_peaks(self):
        image = cp.zeros((5, 5), dtype=cp.uint8)
        image[1, 1] = 20
        image[3, 3] = 10
        peaks = peak.peak_local_max(image, min_distance=1)
        assert peaks.tolist() == [[1, 1], [3, 3]]

        image = cp.zeros((3, 10))
        # Note: CuPy doesn't support this type of indexing
        #       image[1, (1, 3, 5, 7)] = (1, 2, 3, 4)
        image[1, 1] = 1
        image[1, 3] = 2
        image[1, 5] = 3
        image[1, 7] = 4
        peaks = peak.peak_local_max(image, min_distance=1)
        assert peaks.tolist() == [[1, 7], [1, 5], [1, 3], [1, 1]]

    def test_num_peaks(self):
        image = cp.zeros((7, 7), dtype=cp.uint8)
        image[1, 1] = 10
        image[1, 3] = 11
        image[1, 5] = 12
        image[3, 5] = 8
        image[5, 3] = 7
        assert (
            len(peak.peak_local_max(image, min_distance=1, threshold_abs=0))
            == 5
        )
        peaks_limited = peak.peak_local_max(
            image, min_distance=1, threshold_abs=0, num_peaks=2
        )
        assert len(peaks_limited) == 2
        peaks_limited = cp.asnumpy(peaks_limited)
        assert (1, 3) in peaks_limited
        assert (1, 5) in peaks_limited

        peaks_limited = peak.peak_local_max(
            image, min_distance=1, threshold_abs=0, num_peaks=4
        )

        peaks_limited = cp.asnumpy(peaks_limited)
        assert len(peaks_limited) == 4
        assert (1, 3) in peaks_limited
        assert (1, 5) in peaks_limited
        assert (1, 1) in peaks_limited
        assert (3, 5) in peaks_limited

    def test_num_peaks_and_labels(self):
        image = cp.zeros((7, 7), dtype=cp.uint8)
        labels = cp.zeros((7, 7), dtype=cp.uint8) + 20
        image[1, 1] = 10
        image[1, 3] = 11
        image[1, 5] = 12
        image[3, 5] = 8
        image[5, 3] = 7
        peaks_limited = peak.peak_local_max(
            image, min_distance=1, threshold_abs=0, labels=labels
        )
        assert len(peaks_limited) == 5
        peaks_limited = peak.peak_local_max(
            image, min_distance=1, threshold_abs=0, labels=labels, num_peaks=2
        )
        assert len(peaks_limited) == 2

    def test_num_peaks_tot_vs_labels_4quadrants(self):
        np.random.seed(21)
        image = cp.asarray(np.random.uniform(size=(20, 30)))
        i, j = cp.mgrid[0:20, 0:30]
        labels = 1 + (i >= 10) + (j >= 15) * 2
        result = peak.peak_local_max(image, labels=labels,
                                     min_distance=1, threshold_rel=0,
                                     num_peaks=cp.inf,
                                     num_peaks_per_label=2)
        assert len(result) == 8
        result = peak.peak_local_max(image, labels=labels,
                                     min_distance=1, threshold_rel=0,
                                     num_peaks=cp.inf,
                                     num_peaks_per_label=1)
        assert len(result) == 4
        result = peak.peak_local_max(image, labels=labels,
                                     min_distance=1, threshold_rel=0,
                                     num_peaks=2,
                                     num_peaks_per_label=2)
        assert len(result) == 2

    def test_num_peaks3D(self):
        # Issue 1354: the old code only hold for 2D arrays
        # and this code would die with IndexError
        image = cp.zeros((10, 10, 100))
        image[5, 5, ::5] = cp.arange(20)
        peaks_limited = peak.peak_local_max(image, min_distance=1, num_peaks=2)
        assert len(peaks_limited) == 2

    def test_reorder_labels(self):
        image = cp.asarray(np.random.uniform(size=(40, 60)))
        i, j = cp.mgrid[0:40, 0:60]
        labels = 1 + (i >= 20) + (j >= 30) * 2
        labels[labels == 4] = 5
        i, j = cp.mgrid[-3:4, -3:4]
        footprint = i * i + j * j <= 9
        expected = cp.zeros(image.shape, float)
        for imin, imax in ((0, 20), (20, 40)):
            for jmin, jmax in ((0, 30), (30, 60)):
                expected[imin:imax, jmin:jmax] = ndi.maximum_filter(
                    image[imin:imax, jmin:jmax], footprint=footprint
                )
        expected = expected == image
        with expected_warnings(["indices argument is deprecated"]):
            result = peak.peak_local_max(image, labels=labels, min_distance=1,
                                         threshold_rel=0, footprint=footprint,
                                         indices=False, exclude_border=False)
        assert (result == expected).all()

    def test_indices_with_labels(self):
        image = cp.asarray(np.random.uniform(size=(40, 60)))
        i, j = cp.mgrid[0:40, 0:60]
        labels = 1 + (i >= 20) + (j >= 30) * 2
        i, j = cp.mgrid[-3:4, -3:4]
        footprint = i * i + j * j <= 9
        expected = cp.zeros(image.shape, float)
        for imin, imax in ((0, 20), (20, 40)):
            for jmin, jmax in ((0, 30), (30, 60)):
                expected[imin:imax, jmin:jmax] = ndi.maximum_filter(
                    image[imin:imax, jmin:jmax], footprint=footprint
                )
        expected = cp.stack(cp.nonzero(expected == image), axis=-1)
        expected = expected[cp.argsort(image[tuple(expected.T)])[::-1]]
        result = peak.peak_local_max(image, labels=labels, min_distance=1,
                                     threshold_rel=0, footprint=footprint,
                                     exclude_border=False)
        result = result[cp.argsort(image[tuple(result.T)])[::-1]]
        assert (result == expected).all()

    def test_ndarray_indices_false(self):
        nd_image = cp.zeros((5, 5, 5))
        nd_image[2, 2, 2] = 1
        with expected_warnings(["indices argument is deprecated"]):
            peaks = peak.peak_local_max(nd_image, min_distance=1,
                                        indices=False)
        assert (peaks == nd_image.astype(bool)).all()

    def test_ndarray_exclude_border(self):
        nd_image = cp.zeros((5, 5, 5))
        nd_image[[1, 0, 0], [0, 1, 0], [0, 0, 1]] = 1
        nd_image[3, 0, 0] = 1
        nd_image[2, 2, 2] = 1
        expected = cp.zeros_like(nd_image, dtype=bool)
        expected[2, 2, 2] = True
        expectedNoBorder = np.zeros_like(nd_image, dtype=bool)
        expectedNoBorder[2, 2, 2] = True
        expectedNoBorder[0, 0, 1] = True
        expectedNoBorder[3, 0, 0] = True
        expectedNoBorder = cp.asarray(expectedNoBorder)
        with expected_warnings(["indices argument is deprecated"]):
            result = peak.peak_local_max(nd_image, min_distance=2,
                                         exclude_border=2, indices=False)
            assert_array_equal(result, expected)
            # Check that bools work as expected
            assert_array_equal(
                peak.peak_local_max(nd_image, min_distance=2,
                                    exclude_border=2, indices=False),
                peak.peak_local_max(nd_image, min_distance=2,
                                    exclude_border=True, indices=False)
            )
            assert_array_equal(
                peak.peak_local_max(nd_image, min_distance=2,
                                    exclude_border=0, indices=False),
                peak.peak_local_max(nd_image, min_distance=2,
                                    exclude_border=False, indices=False)
            )
            # Check both versions with  no border
            assert_array_equal(
                peak.peak_local_max(nd_image, min_distance=2,
                                    exclude_border=0, indices=False),
                expectedNoBorder,
            )
            assert_array_equal(
                peak.peak_local_max(nd_image,
                                    exclude_border=False, indices=False),
                nd_image.astype(bool)
            )

    def test_empty(self):
        image = cp.zeros((10, 20))
        labels = cp.zeros((10, 20), int)
        with expected_warnings(["indices argument is deprecated"]):
            result = peak.peak_local_max(image, labels=labels,
                                         footprint=cp.ones((3, 3), bool),
                                         min_distance=1, threshold_rel=0,
                                         indices=False, exclude_border=False)
        assert cp.all(~ result)

    def test_empty_non2d_indices(self):
        image = cp.zeros((10, 10, 10))
        result = peak.peak_local_max(image,
                                     footprint=cp.ones((3, 3, 3), bool),
                                     min_distance=1, threshold_rel=0,
                                     exclude_border=False)
        assert result.shape == (0, image.ndim)

    def test_one_point(self):
        image = cp.zeros((10, 20))
        labels = cp.zeros((10, 20), int)
        image[5, 5] = 1
        labels[5, 5] = 1
        with expected_warnings(["indices argument is deprecated"]):
            result = peak.peak_local_max(image, labels=labels,
                                         footprint=cp.ones((3, 3), bool),
                                         min_distance=1, threshold_rel=0,
                                         indices=False, exclude_border=False)
        assert cp.all(result == (labels == 1))

    def test_adjacent_and_same(self):
        image = cp.zeros((10, 20))
        labels = cp.zeros((10, 20), int)
        image[5, 5:6] = 1
        labels[5, 5:6] = 1
        with expected_warnings(["indices argument is deprecated"]):
            result = peak.peak_local_max(image, labels=labels,
                                         footprint=cp.ones((3, 3), bool),
                                         min_distance=1, threshold_rel=0,
                                         indices=False, exclude_border=False)
        assert cp.all(result == (labels == 1))

    def test_adjacent_and_different(self):
        image = cp.zeros((10, 20))
        labels = cp.zeros((10, 20), int)
        image[5, 5] = 1
        image[5, 6] = 0.5
        labels[5, 5:6] = 1
        expected = image == 1
        with expected_warnings(["indices argument is deprecated"]):
            result = peak.peak_local_max(image, labels=labels,
                                         footprint=cp.ones((3, 3), bool),
                                         min_distance=1, threshold_rel=0,
                                         indices=False, exclude_border=False)
        assert cp.all(result == expected)
        with expected_warnings(["indices argument is deprecated"]):
            result = peak.peak_local_max(image, labels=labels,
                                         min_distance=1, threshold_rel=0,
                                         indices=False, exclude_border=False)
        assert cp.all(result == expected)

    def test_not_adjacent_and_different(self):
        image = cp.zeros((10, 20))
        labels = cp.zeros((10, 20), int)
        image[5, 5] = 1
        image[5, 8] = 0.5
        labels[image > 0] = 1
        expected = labels == 1
        with expected_warnings(["indices argument is deprecated"]):
            result = peak.peak_local_max(image, labels=labels,
                                         footprint=cp.ones((3, 3), bool),
                                         min_distance=1, threshold_rel=0,
                                         indices=False, exclude_border=False)
        assert cp.all(result == expected)

    def test_two_objects(self):
        image = cp.zeros((10, 20))
        labels = cp.zeros((10, 20), int)
        image[5, 5] = 1
        image[5, 15] = 0.5
        labels[5, 5] = 1
        labels[5, 15] = 2
        expected = labels > 0
        with expected_warnings(["indices argument is deprecated"]):
            result = peak.peak_local_max(image, labels=labels,
                                         footprint=cp.ones((3, 3), bool),
                                         min_distance=1, threshold_rel=0,
                                         indices=False, exclude_border=False)
        assert cp.all(result == expected)

    def test_adjacent_different_objects(self):
        image = cp.zeros((10, 20))
        labels = cp.zeros((10, 20), int)
        image[5, 5] = 1
        image[5, 6] = 0.5
        labels[5, 5] = 1
        labels[5, 6] = 2
        expected = labels > 0
        with expected_warnings(["indices argument is deprecated"]):
            result = peak.peak_local_max(image, labels=labels,
                                         footprint=cp.ones((3, 3), bool),
                                         min_distance=1, threshold_rel=0,
                                         indices=False, exclude_border=False)
        assert cp.all(result == expected)

    def test_four_quadrants(self):
        image = cp.asarray(np.random.uniform(size=(20, 30)))
        i, j = cp.mgrid[0:20, 0:30]
        labels = 1 + (i >= 10) + (j >= 15) * 2
        i, j = cp.mgrid[-3:4, -3:4]
        footprint = i * i + j * j <= 9
        expected = cp.zeros(image.shape, float)
        for imin, imax in ((0, 10), (10, 20)):
            for jmin, jmax in ((0, 15), (15, 30)):
                expected[imin:imax, jmin:jmax] = ndi.maximum_filter(
                    image[imin:imax, jmin:jmax], footprint=footprint
                )
        expected = expected == image
        with expected_warnings(["indices argument is deprecated"]):
            result = peak.peak_local_max(image, labels=labels,
                                         footprint=footprint,
                                         min_distance=1,
                                         threshold_rel=0,
                                         indices=False,
                                         exclude_border=False)
        assert cp.all(result == expected)

    def test_disk(self):
        """regression test of img-1194, footprint = [1]
        Test peak.peak_local_max when every point is a local maximum
        """
        image = cp.asarray(np.random.uniform(size=(10, 20)))
        footprint = cp.asarray([[1]])
        with expected_warnings(["indices argument is deprecated"]):
            result = peak.peak_local_max(image, labels=cp.ones((10, 20), int),
                                         footprint=footprint,
                                         min_distance=1, threshold_rel=0,
                                         threshold_abs=-1, indices=False,
                                         exclude_border=False)
        assert cp.all(result)
        with expected_warnings(["indices argument is deprecated"]):
            result = peak.peak_local_max(image, footprint=footprint,
                                         threshold_abs=-1,
                                         indices=False,
                                         exclude_border=False)
        assert cp.all(result)

    def test_3D(self):
        image = cp.zeros((30, 30, 30))
        image[15, 15, 15] = 1
        image[5, 5, 5] = 1
        assert_array_equal(
            peak.peak_local_max(image, min_distance=10, threshold_rel=0),
            [[15, 15, 15]],
        )
        assert_array_equal(
            peak.peak_local_max(image, min_distance=6, threshold_rel=0),
            [[15, 15, 15]],
        )
        assert sorted(peak.peak_local_max(image, min_distance=10,
                                          threshold_rel=0,
                                          exclude_border=False).tolist()) == \
            [[5, 5, 5], [15, 15, 15]]
        assert sorted(peak.peak_local_max(image, min_distance=5,
                                          threshold_rel=0).tolist()) == \
            [[5, 5, 5], [15, 15, 15]]

    def test_4D(self):
        image = cp.zeros((30, 30, 30, 30))
        image[15, 15, 15, 15] = 1
        image[5, 5, 5, 5] = 1
        assert_array_equal(
            peak.peak_local_max(image, min_distance=10, threshold_rel=0),
            [[15, 15, 15, 15]],
        )
        assert_array_equal(
            peak.peak_local_max(image, min_distance=6, threshold_rel=0),
            [[15, 15, 15, 15]],
        )
        assert sorted(
            peak.peak_local_max(
                image, min_distance=10, threshold_rel=0, exclude_border=False
            ).tolist()
        ) == [[5, 5, 5, 5], [15, 15, 15, 15]]
        assert sorted(
            peak.peak_local_max(image, min_distance=5, threshold_rel=0).tolist()
        ) == [[5, 5, 5, 5], [15, 15, 15, 15]]

    def test_threshold_rel_default(self):
        image = cp.ones((5, 5))

        image[2, 2] = 1
        assert len(peak.peak_local_max(image)) == 0

        image[2, 2] = 2
        assert_array_equal(peak.peak_local_max(image), [[2, 2]])

        image[2, 2] = 0
        with expected_warnings(["When min_distance < 1"]):
            assert len(peak.peak_local_max(image,
                                           min_distance=0)) == image.size - 1


@pytest.mark.parametrize(
    ["indices"],
    [[indices] for indices in itertools.product(range(5), range(5))],
)
def test_exclude_border(indices):
    image = cp.zeros((5, 5))
    image[indices] = 1

    # exclude_border = False, means it will always be found.
    assert len(peak.peak_local_max(image, exclude_border=False)) == 1

    # exclude_border = 0, means it will always be found.
    assert len(peak.peak_local_max(image, exclude_border=0)) == 1

    # exclude_border = True, min_distance=1 means it will be found unless it's
    # on the edge.
    if indices[0] in (0, 4) or indices[1] in (0, 4):
        expected_peaks = 0
    else:
        expected_peaks = 1
    assert len(peak.peak_local_max(
        image, min_distance=1, exclude_border=True)) == expected_peaks

    # exclude_border = (1, 0) means it will be found unless it's on the edge of
    # the first dimension.
    if indices[0] in (0, 4):
        expected_peaks = 0
    else:
        expected_peaks = 1
    assert len(peak.peak_local_max(
        image, exclude_border=(1, 0))) == expected_peaks

    # exclude_border = (0, 1) means it will be found unless it's on the edge of
    # the second dimension.
    if indices[1] in (0, 4):
        expected_peaks = 0
    else:
        expected_peaks = 1
    assert len(peak.peak_local_max(
        image, exclude_border=(0, 1))) == expected_peaks


def test_exclude_border_errors():
    image = cp.zeros((5, 5))

    # exclude_border doesn't have the right cardinality.
    with pytest.raises(ValueError):
        assert peak.peak_local_max(image, exclude_border=(1,))

    # exclude_border doesn't have the right type
    with pytest.raises(TypeError):
        assert peak.peak_local_max(image, exclude_border=1.0)

    # exclude_border is a tuple of the right cardinality but contains
    # non-integer values.
    with pytest.raises(ValueError):
        assert peak.peak_local_max(image, exclude_border=(1, 'a'))

    # exclude_border is a tuple of the right cardinality but contains a
    # negative value.
    with pytest.raises(ValueError):
        assert peak.peak_local_max(image, exclude_border=(1, -1))

    # exclude_border is a negative value.
    with pytest.raises(ValueError):
        assert peak.peak_local_max(image, exclude_border=-1)


class TestProminentPeaks(unittest.TestCase):
    def test_isolated_peaks(self):
        image = cp.zeros((15, 15))
        x0, y0, i0 = (12, 8, 1)
        x1, y1, i1 = (2, 2, 1)
        x2, y2, i2 = (5, 13, 1)
        image[y0, x0] = i0
        image[y1, x1] = i1
        image[y2, x2] = i2
        out = peak._prominent_peaks(image)
        assert len(out[0]) == 3
        for i, x, y in zip(out[0], out[1], out[2]):
            self.assertTrue(i in (i0, i1, i2))
            self.assertTrue(x in (x0, x1, x2))
            self.assertTrue(y in (y0, y1, y2))

    def test_threshold(self):
        image = cp.zeros((15, 15))
        x0, y0, i0 = (12, 8, 10)
        x1, y1, i1 = (2, 2, 8)
        x2, y2, i2 = (5, 13, 10)
        image[y0, x0] = i0
        image[y1, x1] = i1
        image[y2, x2] = i2
        out = peak._prominent_peaks(image, threshold=None)
        assert len(out[0]) == 3
        for i, x, y in zip(out[0], out[1], out[2]):
            self.assertTrue(i in (i0, i1, i2))
            self.assertTrue(x in (x0, x1, x2))
        out = peak._prominent_peaks(image, threshold=9)
        assert len(out[0]) == 2
        for i, x, y in zip(out[0], out[1], out[2]):
            self.assertTrue(i in (i0, i2))
            self.assertTrue(x in (x0, x2))
            self.assertTrue(y in (y0, y2))

    def test_peaks_in_contact(self):
        image = cp.zeros((15, 15))
        x0, y0, i0 = (8, 8, 1)
        x1, y1, i1 = (7, 7, 1)  # prominent peak
        x2, y2, i2 = (6, 6, 1)
        image[y0, x0] = i0
        image[y1, x1] = i1
        image[y2, x2] = i2
        out = peak._prominent_peaks(image, min_xdistance=3, min_ydistance=3)
        assert_array_equal(out[0], cp.asarray((i1,)))
        assert_array_equal(out[1], cp.asarray((x1,)))
        assert_array_equal(out[2], cp.asarray((y1,)))

    def test_input_labels_unmodified(self):
        image = cp.zeros((10, 20))
        labels = cp.zeros((10, 20), int)
        image[5, 5] = 1
        labels[5, 5] = 3
        labelsin = labels.copy()
        with expected_warnings(["indices argument is deprecated"]):
            peak.peak_local_max(image, labels=labels,
                                footprint=cp.ones((3, 3), bool),
                                min_distance=1, threshold_rel=0,
                                indices=False, exclude_border=False)
        assert cp.all(labels == labelsin)

    def test_many_objects(self):
        mask = np.zeros([500, 500], dtype=bool)
        x, y = np.indices((500, 500))
        x_c = x // 20 * 20 + 10
        y_c = y // 20 * 20 + 10
        mask[(x - x_c) ** 2 + (y - y_c) ** 2 < 8 ** 2] = True
        labels, num_objs = ndimage_cpu.label(mask)
        dist = ndimage_cpu.distance_transform_edt(mask)

        dist = cp.asarray(dist)
        labels = cp.asarray(labels)
        local_max = peak.peak_local_max(dist, min_distance=20,
                                        exclude_border=False, labels=labels)

        assert len(local_max) == 625
