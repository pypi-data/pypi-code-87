from pollination_dsl.alias import OutputAlias
from queenbee.io.common import IOAliasHandler


"""Alias for daylight factor recipe output."""
daylight_factor_results = [
    OutputAlias.any(
        name='results',
        description='Daylight factor values. These can be plugged into the "LB '
        'Spatial Heatmap" component along with meshes of the sensor grids to '
        'visualize results.',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_df_from_folder'
            )
        ]
    ),
    
    # Revit alias
    OutputAlias.any(
        name='results',
        description='Daylight factor values.',
        platform=['revit'],
        handler=[
            IOAliasHandler(
                language='csharp',
                module='Pollination.RevitHandlers',
                function='ReadDaylightFactorResultsFromFolder'
            ),

            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_df_from_folder'
            )
        ]
    ),

    # Rhino alias
    OutputAlias.linked(
        name='results',
        platform=['rhino'],
        handler=[
            # Preload results 
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_df_from_folder'
            ),
            # load preloaded outputs to Rhino with following method
            IOAliasHandler(
                language='csharp', module='Pollination.RhinoHandlers',
                function='LoadMeshBasedResultsToRhino'
            )
        ]
    )
]


"""Point-in-time grid-based results."""
point_in_time_grid_results = [
    OutputAlias.any(
        name='results',
        description='Numbers for the point-in-time value at each sensor. These can be '
        'plugged into the "LB Spatial Heatmap" component along with meshes of the '
        'sensor grids to visualize results. Values are in the standard SI '
        'units of the requested input metric.\n* illuminance = lux'
        '\n* irradiance = W/m2\n* luminance = cd/m2\n* radiance = W/m2-sr',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_pit_from_folder'
            )
        ]
    )
]


"""Point-in-time view-based results."""
point_in_time_view_results = [
    OutputAlias.any(
        name='results',
        description='High Dynamic Range (HDR) images for each View in the model. These '
        'can be plugged into the Ladybug "Image Viewer" component to preview the image. '
        'They can also be plugged into the "HB False Color" component to convert '
        'the image into a false color version. Lastly, it can be connected to '
        'the "HB HDR to GIF" component to get a GIF image that is more portable '
        'and easily previewed by different software. Pixel values are '
        'in the standard SI units of the requested input metric.\n* illuminance = lux'
        '\n* irradiance = W/m2\n* luminance = cd/m2\n* radiance = W/m2-sr',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_images_from_folder'
            )
        ]
    )
]


"""Cumulative sun hours output from the direct sun hours recipe."""
cumulative_sun_hour_results = [
    OutputAlias.any(
        name='hours',
        description='The cumulative number of timesteps that each sensor sees the sun. '
        'If the input wea timestep is 1 (the default), then this is the number of '
        'direct sun hours for each sensor. These can be plugged into the "LB '
        'Spatial Heatmap" component along with meshes of the sensor grids to '
        'visualize results.',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_hours_from_folder'
            )
        ]
    )
]


"""Direct sun hours recipe output."""
direct_sun_hours_results = [
    OutputAlias.any(
        name='results',
        description='Raw result files (.ill) that contain the number of timesteps '
        'that each sensor is exposed to sun. The units are the timestep of '
        'input wea file. For an hourly wea, each value corresponds to an hour '
        'of direct sun.',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='sort_ill_from_folder'
            )
        ]
    )
]


"""Annual daylight recipe output."""
annual_daylight_results = [
    OutputAlias.any(
        name='results',
        description='Raw result files (.ill) that contain illuminance matrices.',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='sort_ill_from_folder'
            )
        ]
    )
]


daylight_autonomy_results = [
    OutputAlias.any(
        name='DA',
        description='Daylight autonomy values for each sensor. These can be plugged '
        'into the "LB Spatial Heatmap" component along with meshes of the sensor '
        'grids to visualize results.',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_da_from_folder'
            )
        ]
    ),
    # Rhino alias
    OutputAlias.linked(
        name='DA Results',
        platform=['rhino'],
        handler=[
            # Preload results 
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_da_from_folder'
            ),
            # load preloaded outputs to Rhino with following method
            IOAliasHandler(
                language='csharp', module='Pollination.RhinoHandlers',
                function='LoadMeshBasedResultsToRhino'
            )
        ]
    )
]


continuous_daylight_autonomy_results = [
    OutputAlias.any(
        name='cDA',
        description='Continuous daylight autonomy values for each sensor. These can '
        'be plugged into the "LB Spatial Heatmap" component along with meshes of '
        'the sensor grids to visualize results.',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_cda_from_folder'
            )
        ]
    ),
    # Rhino alias
    OutputAlias.linked(
        name='cDA Results',
        platform=['rhino'],
        handler=[
            # Preload results 
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_cda_from_folder'
            ),
            # load preloaded outputs to Rhino with following method
            IOAliasHandler(
                language='csharp', module='Pollination.RhinoHandlers',
                function='LoadMeshBasedResultsToRhino'
            )
        ]
    )
]


udi_results = [
    OutputAlias.any(
        name='UDI',
        description='Useful daylight autonomy values for each sensor. These can be '
        'plugged into the "LB Spatial Heatmap" component along with meshes of the '
        'sensor grids to visualize results.',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_udi_from_folder'
            )
        ]
    ),
    # Rhino alias
    OutputAlias.linked(
        name='UDI Results',
        platform=['rhino'],
        handler=[
            # Preload results 
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_udi_from_folder'
            ),
            # load preloaded outputs to Rhino with following method
            IOAliasHandler(
                language='csharp', module='Pollination.RhinoHandlers',
                function='LoadMeshBasedResultsToRhino'
            )
        ]
    )
]


udi_lower_results = [
    OutputAlias.any(
        name='UDI_low',
        description='Values for the percent of time that is below the lower threshold '
        'of useful daylight illuminance. These can be plugged into the "LB '
        'Spatial Heatmap" component along with meshes of the sensor grids to '
        'visualize results.',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_udi_from_folder'
            )
        ]
    ),
    # Rhino alias
    OutputAlias.linked(
        name='UDI low Results',
        platform=['rhino'],
        handler=[
            # Preload results 
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_udi_from_folder'
            ),
            # load preloaded outputs to Rhino with following method
            IOAliasHandler(
                language='csharp', module='Pollination.RhinoHandlers',
                function='LoadMeshBasedResultsToRhino'
            )
        ]
    )
]


udi_upper_results = [
    OutputAlias.any(
        name='UDI_up',
        description='Values for the percent of time that is above the upper threshold '
        'of useful daylight illuminance. These can be plugged into the "LB '
        'Spatial Heatmap" component along with meshes of the sensor grids to '
        'visualize results.',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_udi_from_folder'
            )
        ]
    ),
    # Rhino alias
    OutputAlias.linked(
        name='UDI up Results',
        platform=['rhino'],
        handler=[
            # Preload results 
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='read_udi_from_folder'
            ),
            # load preloaded outputs to Rhino with following method
            IOAliasHandler(
                language='csharp', module='Pollination.RhinoHandlers',
                function='LoadMeshBasedResultsToRhino'
            )
        ]
    )
]


"""Total Radiation results from the Annual Radiation recipe."""
total_radiation_results = [
    OutputAlias.any(
        name='total',
        description='Raw result files (.ill) that contain irradiance matrices '
        'for the total radiation at each sensor and timestep.',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='sort_ill_from_folder'
            )
        ]
    )
]


"""Direct Radiation results from the Annual Radiation recipe."""
direct_radiation_results = [
    OutputAlias.any(
        name='direct',
        description='Raw result files (.ill) that contain irradiance matrices '
        'for the direct radiation at each sensor and timestep.',
        platform=['grasshopper'],
        handler=[
            IOAliasHandler(
                language='python',
                module='pollination_handlers.outputs.daylight',
                function='sort_ill_from_folder'
            )
        ]
    )
]
