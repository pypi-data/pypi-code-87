#!/usr/bin/python
# main.py

# flake8: noqa

"""
Geonomics
=========

Provides:
1. A function for creating custom-structured, editable parameters files.
2. A function for creating model objects from parameters files.
3. Functions for running models.
4. Functions for model visualization.
5. A variety of parameters, for construction of arbitrarily complex simulation scenarios.

How to use the documentation
----------------------------
There are two levels of documentation available:
- Basic, procedural documentation is available as docstrings in the code,
which are returned when requesting Python's help on a class or function.
- Detailed documentation is available at the
`Geonomics homepage <https://geonomics.readthedocs.io/en/latest/>`_.

All documentation examples assume that `geonomics` has been imported as `gnx`::

    >>> import geonomics as gnx

To get help, call Python's `help` function on a component of Geonomics that you
are trying to use, such as::

    >>> help(gnx.make_parameters_file)

Or use the question mark, if you are working in the
`IPython <https://ipython.org>`_ shell or in the
`Jupyter <https://jupyter.org/>`_ Notebook::

    >>> geonomics.make_parameters_file?
"""
#geonomics imports
from geonomics.sim.model import Model
from geonomics.sim.params import (_read_params_file, _make_params_file,
                                  ParametersDict)
from geonomics.structs.landscape import _make_landscape
from geonomics.structs.genome import _make_genomic_architecture
from geonomics.structs.individual import _make_individual
from geonomics.structs.species import _make_species
from geonomics.structs.community import _make_community
from geonomics.structs import landscape, genome, individual, species, community
from geonomics import demos

#other imports
import re
import os, sys, traceback
from collections import Counter as C
import numpy as np
import pandas as pd


######################################
# -----------------------------------#
# CLASSES ---------------------------#
# -----------------------------------#
######################################


######################################
# -----------------------------------#
# FUNCTIONS -------------------------#
# -----------------------------------#
######################################

#wrapper around params.make_parameters_file
def make_parameters_file(filepath=None, layers=1, species=1, data=False,
        stats=False):
    """
    Create a new parameters file.

    Write to disk a new, template parameters file. The file will contain the
    numbers and types of sections indicated by the parameters fed to this
    function. The new file can then be used 'out of the box'
    to make a new Model object, but typically it will be
    edited by the user to stipulate the scenario being simulated,
    then used to instantiate a Model.

    Parameters
    ----------
    filepath : str, optional, default: None
        Where to write the resulting parameters file, in /path/to/filename.py
        format. Defaults to None. If None, a file named
        "GNX_params_<datetime>.py" will be written to the working
        directory.

    layers : {int, list of dicts}, optional, default: 1
        Number (and optionally, types) of Layer-parameter sections to include
        in the parameters file that is generated. Defaults to 1. Valid values
        and their associated behaviors are:

        *If an int is passed*:
            Add sections for the stipulated number of Layers, each with default
            settings:
                - parameters for creating Layers of type 'random' (i.e.
                  Layers that will be generated by interpolation from
                  randomly valued random points)
                - no LandscapeChanger parameters

        *If [dict, ..., dict] is passed*:
            Each dict in this list should have the following key-value pairs:
                KEY                    VALUE
                'type':                {'random', 'defined', 'file', 'nlmpy'}

                'change':               bool

            This will add one section of Layer parameters, with the
            contents indicated, for each dict in this list.

    species : {int, list of dicts}, optional, default: 1
        Number (and optionally, types) of Species-parameter sections to
        include in the parameters file that is generated. Defaults to 1. Valid
        values and their associated behaviors are:

        *If an int is passed*:
            Add sections for the stipulated number of Species, each with
            default settings:
                - parameters for movement and dispersal without
                  _ConductanceSurfaces
                - parameters for a GenomicArchitecture with 0 Traits (i.e. with
                  only neutral loci)
                - no _SpeciesChanger parameters

        *If [dict, ..., dict] is passed*:
            Each dict in this list can contain any of the following
            key-value pairs:
                KEY                     VALUE

                'movement':             bool,

                'movement_surface':     bool,

                'dispersal_surface':    bool,

                'genomes':              {bool, 'custom'},

                'n_traits':             int,

                'demographic_change':   int,

                'parameter_change':     bool

            This will add one section of Species parameters, customized
            as indicated, for each dict in the list. (Note that if the
            'genomes' argument is True or 'custom', a section for
            parameterization of the genomic architecture will be added,
            but if it is 'custom' then a template custom genomic architecture
            file will also be created (a CSV file), which can be filled in
            to stipulate the locus-wise values for starting allele frequency,
            recombination rate, dominance, associated traits, and effect
            sizes.)

    data : bool, optional, default: False
        Whether to include a Data-parameter section in the parameters file that
        is generated. Defaults to None. Valid values and their associated
        behaviors are:

        None, False:
            Will not add a section for parameterizing data to be collected.
            No _DataCollector will be created for the Model object made from
            the resulting parameters file, and no data will be collected
            during the model runs.
        True:
            Will add a section that can be used to parameterize which
            data will be collected during the model runs, when, and what
            file formats will be used to write it to disk.
            (This which will be managed by the model's _DataCollector
            object.)

    stats : bool, optional, default: False
        Whether to include a Stats-parameter section in the parameters file that
        is generated. Defaults to None. Valid values and their associated
        behaviors are:

        None, False:
            Will not add a section for parameterizing the statistics to be
            calculated. No _StatsCollector will be created for the Model
            object made from the resulting parameters file, and no
            statistics will be calculated during the model runs.
        True:
            Will add a section that can be used to parameterize which
            statistics will be calculated during the model runs, and when.
            (This will be managed by the model's _StatsCollector object.)

    Returns
    -------
    None
        Returns no output. Resulting parameters file will be written to the
        location and filename indicated (or by default, will be written to a
        file named "GNX_params_<datetime>.py" in the working directory).

    See Also
    --------
    sim.params.make_parameters_file

    Notes
    -----
    All parameters of this function are optional. Calling the function without
    providing any parameters will always produce the parameters file for the
    default model scenario. This file can be instantiated as a Model object and
    run without being edited. Those three steps (create default parameters file;
    create model from that parameters file; run the model) serve as a base case
    to test successful package installation, and are wrapped around by the
    convenience function `gnx.run_default_model`.

    Examples
    --------
    In the simplest example, we can create a parameters file for the default
    model. Then (assuming it is the only Geonomics parameters file in the
    current working directory, so that it can be unambiguously identified) we
    can call the gnx.make_model function to create a Model object from that
    file, and then call the Model.run method to run the model (setting the
    'verbose' parameter to True, so that we can observe model output).

    >>> gnx.make_parameters_file()
    >>> mod = gnx.make_model()

    NOTE: Using the following file, in the current working directory to create the Model object:
            GNX_params_21-01-2020_17:22:08.py

    >>> mod.run(verbose = True)
    ###############################################################################################
    Running model "GNX_params_21-01-2020_17:22:08"...
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Setting up iteration 0...
    Creating the burn-in function queue...
    Creating the main function queue...
    Running burn-in, iteration 0...
    burn:   it=0:   t=0
            species: spp_0                         N=250    (births=35      deaths=214)
    .......................................................................................
    burn:   it=0:  t=1
            species: spp_0                         N=250    (births=35      deaths=214)
    .......................................................................................
    burn:   it=0:  t=2
            species: spp_0                         N=250    (births=35      deaths=214)
    .......................................................................................
    .
    .
    .


    We could also use some of this function's arguments, to create a parameters
    file for a model with 3 Layers and 1 Species (all with the default
    components for their sections of the parameters file) and with a section
    for parameterizing data collection.

    >>> gnx.make_parameters_file(layers = 3, data = True)

    As a more complex example that is likely to be similar to most use cases,
    we can create a parameters file for a model scenario with:
        - 2 Layers (one being an nlmpy Layer that will not change over model
          time, the other being a raster read in from a GIS file and being
          subject to change over model time);
        - 2 Species (the first having genomes, 2 Traits, and movement
          that is dictated by a _ConductanceSurface; the second not having
          genomes but having dispersal determined by a
          _ConductanceSurface, and undergoing
          demographic change)
        - data-collection;
        - stats-collection;
    We can save this to a file named "2-spp_2-trait_model.py" in our current
    working directory.

    >>> gnx.make_parameters_file(
    >>>     #list of 2 dicts, each containing the values for each Layer's
    >>>     #parameters section
    >>>     layers = [
    >>>         {'type': 'nlmpy'},                              #layer 1 
    >>>         {'type': 'gis',                                 #layer 2 
    >>>          'change': True}
    >>>         ],
    >>>     #list of 2 dicts, each containing the values for each Species's
    >>>     #parameters section
    >>>     species = [
    >>>         {'genomes': True,                               #spp 1
    >>>          'n_traits': 2,
    >>>          'movement': True,
    >>>          'movement_surface': True},
    >>>         {'genomes': False,                              #spp 2
    >>>          'movement': True,
    >>>          'dispersal_surface': True,
    >>>          'demographic_change': True}
    >>>         ],
    >>>     #arguments to the data and stats parameters
    >>>     data = True, stats = True,
    >>>     #destination to which to write the resulting parameter file
    >>>     filepath = '2-spp_2-trait_model.py')

    """

    #check if any keys in the layers or species dicts are abnormal, and
    #provide warning if so
    valid_l_keys = ['type', 'change']
    valid_p_keys = ['movement', 'movement_surface', 'dispersal_surface',
        'genomes', 'n_traits', 'custom_genomic_architecture',
        'demographic_change', 'parameter_change']
    if isinstance(layers, list):
        for n, lyr_dict in enumerate(layers):
            if False in [k in valid_l_keys for k in lyr_dict.keys()]:
                invalid_keys = ', '.join([k for k in lyr_dict.keys(
                    ) if k not in valid_l_keys])
                err_msg = ("One or more of the keys in dict number %i of "
                    "the 'layers' argument is not valid. Invalid values: "
                    "%s.") % (n, invalid_keys)
                print('')
                raise ValueError(err_msg)
    if isinstance(species, list):
        for n, spp_dict in enumerate(species):
            if False in [k in valid_p_keys for k in spp_dict.keys()]:
                invalid_keys = ', '.join([k for k in spp_dict.keys(
                    ) if k not in valid_p_keys])
                err_msg = ("One or more of the keys in dict number %i of "
                    "the 'species' argument is not valid. Invalid values: "
                    "%s.") % (n, invalid_keys)
                raise ValueError(err_msg)

    _make_params_file(filepath=filepath, layers=layers, species=species,
                      data=data, stats=stats)


#wrapper around params.read
def read_parameters_file(filepath):
    """
    Create a new ParametersDict object.

    Read the Geonomics parameters file saved at the location indicated by
    'filepath', check its validity (i.e. that all the Layers and Species
    parameterized in that file have been given distinct names), then use the
    file to instantiate a ParametersDict object.

    Parameters
    ----------
    filepath : str
        String indicating the location of the Geonomics parameters file that
        should be made into a ParametersDict object.

    Returns
    -------
    :class:`geonomics.ParametersDict`
        A dict of nested dicts, all of which have key-value pairs whose values
        can be accessed using typical dict notation or using dot notation.
        Can be fed into the geonomics.make_model function to create a
        Geonomics model.


    Raises
    ------
    AssertionError
        If either the Layers or the Species parameterized in the parameters
        file have not all been given distinct names

    See Also
    --------
    sim.params.read
    sim.params.ParametersDict

    Examples
    --------
    Read a parameters file called "null_model.py" (located in the current
    working directory).

    >>> gnx.read_parameters_file('null_model.py')
    <class 'sim.params.ParametersDict'>
    Model name:                                     null_model

    """

    #first read in file as a block of text
    with open(filepath, 'r') as f:
        txt = f.read()
    #find all the layer names and spp names
    lyr_names = re.findall('\S+(?=: \{\n\n\s+#-*#\n\s+#--- layer num\.)', txt)
    lyr_names = [re.sub("'", '"', n) for n in lyr_names]
    spp_names = re.findall('\S+(?=: \{\n\n\s+#-*#\n\s+#--- spp num\.)', txt)
    spp_names = [re.sub("'", '"', n) for n in spp_names]
    #get Counter objects of each
    lyr_name_cts = C(lyr_names)
    spp_name_cts = C(spp_names)
    #assert that each layer name is used only once
    assert set([*lyr_name_cts.values()]) == {1}, ("At least one of the "
        "Layer names provided in the parameters file appears to be used more "
        "than once. Violating names include: %s") % (';'.join([( "'%s', "
        "used %i times.") % (str(k),
                            v) for k, v in lyr_name_cts.items() if v>1]))
    #assert that each spp name is used only once
    assert set([*spp_name_cts.values()]) == {1}, ("At least one of the "
        "Species names provided in the parameters file appears to be used "
        "more than once. Violating names include: %s") % (';'.join([("'%s', "
            "used %i times.") % (
                str(k), v) for k, v in spp_name_cts.items() if v>1]))

    #break the file into sections for each species, then check that
    #trait names are only used once within each spp
    spp_sects = re.split('#spp name', txt)
    for sect in spp_sects:
        trt_names = re.findall('\S+(?=: \{\n\s+#trait-selection)', sect)
        if len(trt_names) > 0:
            trt_names = [re.sub("'", '"', n) for n in trt_names]
            trt_name_cts = C(trt_names)
            sect_spp_name = re.findall(
                        '\S+(?=: \{\n\n\s+#-*#\n\s+#--- spp num\.)', txt)[0]
            assert set([*trt_name_cts.values()]) == {1}, ("At least one of the"
                " Trait names provided in the parameters for Species "
                "%s appears to be used more than once. "
                "Violating names include: %s") % (sect_spp_name,
                ';'.join([("'%s', used %i times.") % (str(k),
                v) for k, v in trt_name_cts.items() if v>1]))



    #now read the file in as a ParametersDict object
    params = _read_params_file(filepath)
    return(params)


#function to make a regular dict into a ParametersDict object
def make_params_dict(params, model_name=None):
    """
    Create a ParametersDict object from a dict object.

    Use a plain Python dict object, and an optional model name, to create
    a new ParametersDict object.

    Parameters
    ----------

    params: {dict}
        The plain Python dict that is to be turned into a Geonomics
        ParametersDict object.

    model_name: {str}, optional, default: None
        The name to be assigned to the model. (If not provided, the model
        will be called 'unnamed_model'.)

    Returns
    -------
    :class:`geonomics.ParametersDict`
        A dict of nested dicts, all of which have key-value pairs whose values
        can be accessed using typical dict notation or using dot notation. If
        formatted correctly, can be fed into the geonomics.make_model function
        to create a Geonomics model.


    """
    params_dict=ParametersDict(params)
    if model_name is not None:
        params_dict.model['name'] = model_name
    else:
        params_dict.model['name'] = 'unnamed_model'
    return params_dict


#function to create a model from a ParametersDict object
def make_model(parameters=None, verbose=False):
    """
    Create a new Model object.

    Use either a ParametersDict object or the path to a valid Geonomics
    parameters file (whichever is provided to the 'parameters' argument) to
    create a new Model object.

    Parameters
    ----------
    parameters : {ParametersDict, dict, str}, optional, default: None
        The parameters to be used to make the Model object.

        If `parameters` is a ParametersDict object, the object will be used to
        make the Model.

        If `parameters` is a dict object, Geonomics will attempt to convert it
        to a ParametersDict object, then use that object to make the Model.

        If `parameters` is a string, Geonomics will call
        `gnx.read_parameters_file` to make a ParametersDict object, then use
        that object to make the Model.

        If `parameters` is None, or is not provided, then Geonomics will
        attempt to find a single parameters file in the current working
        directory with the filename "GNX_params_<...>.py", will use that
        file to make a ParametersDict object, then will use that object to
        make the Model.

    Returns
    -------
    :class:`geonomics.Model`
        An object of the Model class

    Raises
    ------
    ValueError
        If the `parameters` argument was not provided and a single, valid
        Geonomics parameters file could not be identified in the current
        working directory
    ValueError
        If the `parameters` arugment was given a string that does not point
        to a valid parameters file
    ValueError
        If the ParametersDict provided to the `parameters` argument, or created
        from the parameters file being used, cannot be successfully made into a
        Model

    See Also
    --------
    gnx.read_parameters_file
    sim.model.Model

    Examples
    --------
    Make a Model from a single, valid "GNX_params_<...>.py" file that can
    be found in the current working directory (such as a file that would be
    produced by calling gnx.make_parameters_file without any arguments).

    >>> gnx.make_model()
    <class 'sim.model.Model'>
    Model name:                                     GNX_params_13-10-2018_15:54:03
    Layers:                                         0: '0'
    Species:                                        0: '0'
    Number of iterations:                           1
    Number of burn-in timesteps (minimum):          30
    Number of main timesteps:                       100
    Geo-data collected:                             {}
    Gen-data collected:                             {}
    Stats collected:                                {}


    Make a Model from a file called 'null_model.py', in the current working
    directory.

    >>> gnx.make_model('null_model.py')
    <class 'sim.model.Model'>
    Model name:                                     null_model
    Layers:                                         0: 'tmp'
                                                    1: 'ppt'
    Species:                                        0: 'C. fasciata'
    Number of iterations:                           2500
    Number of burn-in timesteps (mininum):          100
    Number of main timesteps:                       1000
    Geo-data collected:                             {csv, geotiff}
    Gen-data collected:                             {vcf, fasta}
    Stats collected:                                {maf, ld, mean_fit, het, Nt}

    """

    if parameters is None:
        try:
            params_files = [f for f in os.listdir('.') if (
                f.startswith('GNX_params_')
                and os.path.splitext(f)[1] == '.py')]
            assert len(params_files) == 1, ("The 'parameters' argument was not"
                " provided, and it appears that the current working directory "
                "contains more than one 'GNX_params_<...>.py' file. "
                "Please run again, providing a valid value for the "
                "'parameters' argument.")
            parameters = params_files[0]
            print(("\n\nNOTE: Using the following file, in the current working"
              " directory to create the Model object:\n\t%s\n\n") % parameters)
        except Exception as e:
            raise ValueError(("The 'parameters' argument was not provided, "
                "and Geonomics could not identify a single "
                "'GNX_params_<...>.py' file in the current working "
                "directory from which to create the Model object. The "
                "following error was thrown: %s") % e)

    assert ( (type(parameters) is str and os.path.isfile(parameters))
        or str(type(
            parameters)) == "<class 'geonomics.sim.params.ParametersDict'>"),(
        "If the 'parameters' argument is provided, its value must be either a "
        "string pointing to a valid Geonomics parameters file or an object of "
        "the ParametersDict class. If it is not provided, the current working "
        "directory must contain a single 'GNX_params_<...>.py' file "
        "from which to create the Model object.")

    if type(parameters) is str:
        try:
            parameters = read_parameters_file(parameters)
        except Exception as e:
            traceback.print_exc(file = sys.stdout)
            raise ValueError(("Failed to read the parameters file at the "
                "filepath that was provided. The following error was raised: "
                "\n\t%s\n\n") % e)

    if type(parameters) is dict:
        try:
            parameters = make_params_dict(params, 'unnamed_model')
        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            raise ValueError(("A plain dict was provided as the value for "
                              "the parameters argument, but that dict "
                              "could not be converted to a Geonomics "
                              "ParametersDict object."))

    #elif isinstance(parameters, geonomics.sim.params.ParametersDict):
    else:
        pass
    try:
        name = parameters.model.name
        mod = Model(name, parameters, verbose=verbose)
        return(mod)
    except Exception as e:
            traceback.print_exc(file = sys.stdout)
            raise ValueError(("Failed to create a Model object from the "
                "ParametersDict object being used. "
                "The following error was raised: \n\t%s\n\n") % e)


# convenience function for creating a parameters-file for, instantiating, and
# running the default model, plotting the result, then returning the Model
# object
def run_default_model(delete_params_file=True, animate=False):
    """
    Run the default Geonomics model.

    This will create a parameters file for the default Geonomics model,
    read that in as a model, and run a single iteration of that model.

    Parameters
    ----------
    delete_params_file : bool, optional, default: True
        Whether or not to delete the parameters file used for this model
        after the model has finished running

    animate : bool, optional, default: False
        Whether or not plot the model's species as an animated Matplotlib
        plot while the model is running.

    Returns
    -------
    :class:`geonomics.Model`
        The Model object that was created, after it has run to completion.
        (If saved to a variable, it can be used for any number of additional
        runs using the Model.walk method. It can also be used to try out
        visualization methods, or to introspect its structure.)
    """


    # make the default params file
    filename = 'GNX_default_model_params.py'
    make_parameters_file(filename)
    # create the default model
    mod = make_model(parameters = filename)
    # run the default model in verbose mode
    mod.walk(T=10000, mode='burn', verbose = True, animate=animate)
    mod.walk(T=50, mode='main', verbose=True, animate=animate)
    # plot the results
    mod.plot(0,0,0)
    # get rid of the params file it created
    if delete_params_file:
        os.remove(os.path.join('.', filename))
    # return the model, in case someone wants to mess with/introspect it
    # afterwards
    return mod


# convenience function for creating a parameters-file for, instantiating, and
# running the default model, plotting the result, then returning the Model
# object
def run_demo(name, save_figs=False, time_it=False, **kwargs):
    """
    Run a Geonomics demo.

    This will run whichever of the Geonomics demos is stipulated by the *name*
    argument.

    Parameters
    ----------
    name : str 
        Can be one of the following values:

            - *'IBD IBE'*: Runs the IBD, IBE demo (example 1 from the methods
              paper).

            - *'simult select'*: Runs the simultaneous selection demo (example
              2 from the methods paper).

            - *'Yosemite'*: Runs the Yosemite demo (example 3 from the methods
              paper).

    save_figs : bool, optional, default: False
        If True, all figures that are produced will be saved to their default
        filenames in the current working directory.

    time_it : bool, optional, default: False
        If True, the run time for the main portion of the model (excluding
        calculation of data for figures and creation of figures, as much as
        possible) will be calculated, then displayed after the model has run
        to completion.

    Notes
    -----
    Some of the available demos come from the original Geonomics methods paper,
    Hart and Wang 2020, "Geonomics: forward-time, agent-based, spatially
    explicit, and arbitrarily complex landscape genomic simulations".

    Returns
    -------
    :class:`geonomics.Model`
        The Model object that was created, after it has run to completion.
        (If saved to a variable, it can be used for any number of additional
        runs using the Model.walk method. It can also be used to try out
        visualization methods, or to introspect its structure.)
    """

    if name.lower() == 'ibd ibe':
        params = demos._IBD_IBE._make_params()
        params = make_params_dict(params)
        mod = demos._IBD_IBE._run(params, save_figs, time_it, **kwargs)

    elif name.lower() == 'simult select':
        params = demos._simult_select._make_params()
        params = make_params_dict(params)
        mod = demos._simult_select._run(params, save_figs, time_it, **kwargs)

    elif name.lower() == 'yosemite':
        params = demos._yosemite._make_params()
        params = make_params_dict(params)
        mod = demos._yosemite._run(params, save_figs, time_it, **kwargs)

    else:
        print(('The specified demo ("%s") either is not yet implemented '
               'or does not exist!') % name)
        mod = None

    return mod


# wrapper around landscape.make_landscape
def make_landscape(params):
    """
    Make a Landscape object.

    Use the parameter values stored in the input params argument
    to instantiate a Landscape object.

    Parameters
    ----------
    params : ParametersDict
        A ParametersDict object, such as that output by the
        make_params_dict function.

    Returns
    -------
    :class:`geonomics.structs.landscape.Landscape`
        A Landscape instance.
    """

    land = _make_landscape(params)
    return land


#wrapper around genome.make_genomic_architecture
def make_genomic_architecture(params, landscape):
    """
    Make a GenomicArchitecture object.

    Use the parameter values stored in the input params argument,
    and the Landscape object input as the landscape argument,
    to instantiate a GenomicArchitecture object.

    Parameters
    ----------
    params : ParametersDict
        A ParametersDict object (such as that output by the
        make_params_dict function).

    landscape : Landscape
        A Landscape object (such as that returned by the
        make_landscape function).

    Returns
    -------
    :class:`geonomics.structs.genome.GenomicArchitecture`
        A GenomicArchitecture instance.

    """
    gen_arch = _make_genomic_architecture(params, landscape)
    return gen_arch


#wrapper around individual.make_individual
    #should provide either a new genome for the individual, or a
    #genomic_architecture to use to draw its genome;
    #and should provide either a parental centerpoint to disperse from, or a
    #landscape.dim tuple within which to choose a location;
    #burn can be True (i.e. then the individual will have a [[0,0]] genome)
def make_individual(idx, genomic_architecture=None, new_genome=None, dim=None,
    parental_midpoint=None, sex=None, age=0):
    """
    Make an Individual object.

    Make a new Individual, whose index number, genome,
    location, sex, and age are determined by the input arguments.

    Parameters
    ----------
    idx : int
        The index number to be assigned to the new individual.

    genomic_architecture : GenomicArchitecture, optional
        A GenomicArchitecture object, describing the genomic
        characteristics of the Species to which the Individual belongs.
        If the new_genome argument is not provided then the relevant parameter
        values in the GenomicArchitecture will be used when randomly
        drawing the individual's new genome.

    new_genome : nx2 np.ndarray, optional
        The Individual's genome, as an nx2 Numpy ndarray of 0's and 1's.

    dim : (int, int), optional
        A tuple of the landscape's (x, y) dimensionality, to be used if the
        individual's location is to be randomly randomly drawn from anywhere on
        the landscape (rather than being drawn by dispersal from the parental
        midpoint, which will occur if the parental_midpoint argument is
        provided).

    parental_midpoint : (float, float), optional
        A tuple of the (x,y) continuous coordinates, representing the point
        from which dispersal should occur to determine the individual's
        location. This is normally thought of as the midpoint between the individual's
        two parents, but if you are creating an individual without reference to
        parents then this can also simply be thought of as representing the center of
        the neighborhood into which the individual will disperse.

    sex : int, optional
        An integer representing the individual's sex (0 for female, 1 for
        male). Can be left as None for asexual or non-sexed Species.

    age : int, optional
        An integer representing the number of timesteps for which the
        individual has already survived - hence its age, or stage.

    Returns
    -------
    :class:`geonomics.structs.individual.Individual`
        An Individual instance.
    """
    assert (genomic_architecture is not None
        or new_genome is not None), ("Either a new genome must be provided "
        "(i.e. 'new_genome' must not be None) or a genomic architecture from "
        "which to draw a new genome must be provided (i.e. "
        "'genomic_architecture' must not be None.")
    assert (parental_centerpoint is not None
            or dim is not None), ("Either a Landscape-dimension tuple must be "
            "provided (i.e. 'dim' must not be None) or a parental centerpoint "
            "from which to disperse the individual must be provided (i.e. "
            "'parental_centerpoint' must not be None).")
    ind = _make_individual(idx = idx, offspring = False,
            dim = dim, genomic_architecture = genomic_architecture,
            new_genome = new_genome, sex = sex,
            parental_centerpoint = parental_centerpoint, age = age)
    return ind


#wrapper around species.make_species
    #burn can be True (i.e. then the individuals will have a [[0,0]] genome)
def make_species(landscape, spp_params):
    """
    Make a Species object.

    Use the parameter values stored in the input spp_params argument,
    and the Landscape object input as the landscape argument,
    to instantiate a Species object.

    Parameters
    ----------
    landscape : Landscape
        A Landscape object (such as that returned by the
        make_landscape function).

    spp_params : ParametersDict
        The subsection of a full ParametersDict object (such as that output by the
        make_params_dict function) that pertains to the particular species to
        be created.

    Returns
    -------
    :class:`geonomics.structs.species.Species`
        A Species instance.
    """
    spp = _make_species(landscape, spp_params)
    return(spp)


#wrapper around community.make_comunity
    #burn can be True (i.e. then the individuals will have a [[0,0]] genome)
def make_community(landscape, params):
    """
    Make a Community object.

    Use the parameter values stored in the input params argument,
    and the Landscape object input as the landscape argument,
    to instantiate a Community object.

    Parameters
    ----------
    landscape : Landscape
        A Landscape object (such as that returned by the
        make_landscape function).

    spp_params : ParametersDict
        A ParametersDict object (such as that output by the
        make_params_dict function).

    Returns
    -------
    :class:`geonomics.structs.community.Community`
        A Community instance.
    """
    comm = _make_community(landscape, params)
    return comm
