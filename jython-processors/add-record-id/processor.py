# This file is the actual code for the custom Jython step add-record-id

# global- and project-level variables are passed as a dss_variables dict
### INITIALISATION 
step_project_var = "step"
resource_folder = get_step_resource()
plugin_config = get_plugin_config()
step_config = get_step_config()
        
# Get and Check Input Params 

scenario_name = step_config.get("scenario",None)

loop_type = step_config.get("loop_type", None)
# the step parameters are passed as a params dict

# Define here a function that returns the result of the step.
record_id = 0

def process(row):
    # row is a dict of the row on which the step is applied
    
    return record_id + 1
