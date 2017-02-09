import iris
import cf_units

import ozone_column.toz


def calc_dos(cubes):
    mrso_cube = cubes.extract('mrso')
    msfoc_cube = cubes.extract('mrsofc')
    pass


def calc_lwp(cubes, project, model):
    """
    Liquid water path is calculated by subtracting clivi (ice water) from clwvi
    (condensed water path).

    Note: Some models output the variable "clwvi" which only contains lwp. In
    these cases, the input clwvi cube is just returned.
    
    Args:
        * cubes: cubelist containing clwvi_cube and clivi_cube
        * project
        * model
    Returns:
        Cube containing liquid water path.

    """
    # TODO: find out correct names for clwvi/clivi
    clwvi_cube = cubes.extract('clwvi')
    clivi_cube = cubes.extract('clivi')

    BAD_MODELS = ['CESM1-CAM5-1-FV2', 'CESM1-CAM5', 'CMCC-CESM', 'CMCC-CM',
                  'CMCC-CMS', 'IPSL-CM5A-MR', 'IPSL-CM5A-LR', 'IPSL-CM5B-LR',
                  'CCSM4', 'IPSL-CM5A-MR', 'MIROC-ESM', 'MIROC-ESM-CHEM',
                  'MIROC-ESM', 'CSIRO-Mk3-6-0', 'MPI-ESM-MR', 'MPI-ESM-LR',
                  'MPI-ESM-P']

    if (project in ["CMIP5", "CMIP5_ETHZ"] and model in BAD_MODELS) or \
        (project == 'OBS' and model == 'UWisc'):
            print('lwp:ncl INFO:')
            print("   assuming that variable clwvi from {} model {} contains"
                "only liquid water".format(project, model)
            lwp_cube = clwvi_cube
    else:
        lwp_cube = clwvi_cube - clivi_cube

    # TODO: Rename cube lwp_cube.name('liquid_water_path')
    # TODO: Fix units? lwp_cube.units = cf_units.Unit('kg')
    return lwp_cube


def calc_toz(cubes):
    return ozone_column.toz.total_column_ozone(cubes)

