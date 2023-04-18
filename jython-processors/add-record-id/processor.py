# This file is the actual code for the custom Jython step add-record-id

# global- and project-level variables are passed as a dss_variables dict
### INITIALISATION 
import os, json
from dataiku.customstep import *
from io_utils import *
import re

resource_folder = get_step_resource()
plugin_config = get_plugin_config()
step_config = get_step_config()


start_index_at_1 = step_config.get["start_index_at_1"]

# Define here a function that returns the result of the step.
record_id = 0

def process(row):
    # row is a dict of the row on which the step is applied
    if start_index_at_1:
        
    return record_id + 1
