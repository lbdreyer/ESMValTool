import iris
import cf_units

BAD_MODELS = ['CESM1-CAM5-1-FV2', 'CESM1-CAM5', 'CMCC-CESM', 'CMCC-CM',
              'CMCC-CMS', 'IPSL-CM5A-MR', 'IPSL-CM5A-LR', 'IPSL-CM5B-LR',
              'CCSM4', 'IPSL-CM5A-MR', 'MIROC-ESM', 'MIROC-ESM-CHEM',
              'MIROC-ESM', 'CSIRO-Mk3-6-0', 'MPI-ESM-MR', 'MPI-ESM-LR',
              'MPI-ESM-P']

def liquid_water_path(clwvi_cube, clivi_cube, index):
    """
    Liquid water path is calculated by subtracting clivi (ice water) from clwvi
    (condensed water path).

    Note: Some models output the variable "clwvi" which only contains 
    Args:
        * clwvi_cube: 
        * clivi_cube:
        * index: dictionary containing information 
    Returns:
        Cube containing liquid water path.
    """
    project = index[project]
    model = index[model]

    if project in ["CMIP5", "CMIP5_ETHZ"]:
        if model in BAD_MODELS:
            print('lwp:ncl INFO:')
            print("   assuming that variable clwvi from {} model {} contains"
                  "only liquid water".format(project, model)
            lwp_cube = clwvi_cube - clivi_cube
    if project == 'OBS':
        if model == 'UWisc':
            lwp_cube = 
    else:
        lwp_cube = clwvi_cube - clivi_cube

    # TODO: Rename cube lwp_cube.name('liquid_water_path')
    # TODO: Fix units? lwp_cube.units = cf_units.Unit('kg')
    return lwp_cube

