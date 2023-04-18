# This file is the actual code for the custom Jython step add-record-id
import dataiku
import os, json
from dataiku.customstep import *
from io_utils import *
import re

resource_folder = get_step_resource()
plugin_config = get_plugin_config()
step_config = get_step_config()


start_index_at_1 = step_config.get["start_index_at_1"]

# Define here a function that returns the result of the step.
count = 0
def process(row):
    global record_id
    record_id = count
    if start_index_at_1:
        record_id +=1
    count +=1  
    return record_id
