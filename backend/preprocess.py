# Example of a way to run the derive_variables
# This file must be run in this directory

from collections import namedtuple

import derive_variables as der_var

var_spec = namedtuple('var_spec', 'fn cubes extra')
VARIABLES_LOOKUP = {
    'clt':   var_spec(cubes_in=['clt'],            fn=None, extra=None),        
    'clwvi': var_spec(cubes_in=['clwvi'],          fn=None, extra=None),        
    'dos':   var_spec(cubes_in=['mrso', 'mrsofc'], fn=der_var.calc_dos, extra=None),        
    'lwp':   var_spec(cubes_in=['clwvi', 'clivi'], fn=der_var.calc_lwp, extra=['project', 'model']),  
    'sm':    var_spec(cubes_in=['sm'],             fn=der_var.calc_sm, extra=None),
    'theta': var_spec(cubes_in=['theta'],          fn=der_var.calc_theta, extra=None),
    'toz':   var_spec(cubes_in=['tro3', 'ps'],     fn=der_var.calc_toz, extra=None),
    'tro3':  var_spec(cubes_in=['tro3'],           fn=None, extra=None),        
}
   

def preprocess(project_info, files):
    for diagnostic in project_info['DIAGNOSTICS']:

        for variable in diagnostic['variables']:
            var_spec = VARIABLES_LOOKUP[variable]

            for model in project_info['MODELS']:

                # Load in required cubes
                cubes = iris.load(files, var_spec.cubes_in)

                # Extract time
                cubes = [extract_time(cube) for cube in cubes]

                if var_spec.fn != None:
                    # Derive variable
                    derive_var = var_spec.fn
                    
                    if var_spec.extra != None:
                        extra_args = None
                    else:
                        extra_args = (project, model)
                        
                    cube = derive_var(cubes, extra_args)
                else:
                    cube, = cubes
                
                ## Cube is then fixed, regridded, etc../

## Test
example_proj_info = {
    'DIAGNOSTICS': [
                    {'diag_name': 'Diag1', 'variables': ['toz']},
                    {'diag_name': 'Diag2', 'variables': ['lwp']},
                    {'diag_name': 'Diag3', 'variables': ['tro3']},
                    ],
    'MODELS': ['CCSM4'],
}
preprocess(example_proj_info, files='')
