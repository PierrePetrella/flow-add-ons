import dataiku
import pandas as pd, numpy as np

# Import the helpers for custom recipes
from dataiku.customrecipe import get_input_names_for_role
from dataiku.customrecipe import get_output_names_for_role
from dataiku.customrecipe import get_recipe_config


# Get input output datasets
input_dataset_name = get_input_names_for_role('input_dataset')[0]
input_dataset = dataiku.Dataset(input_dataset_name)

# For outputs, the process is the same:
output_dataset_name = get_output_names_for_role('output_dataset')[0]
output_dataset = dataiku.Dataset(output_dataset_name)
# Get parameters
start_index_at_1 = get_recipe_config()['start_index_at_1']
record_id = get_recipe_config().get('record_id_name', "RecordID")


# Read recipe inputs

df = input_dataset.get_dataframe()

if start_index_at_1 == True:
    df.insert(0,record_id, range(1, len(df.index) + 1))
else:
    df.insert(0,record_id, range(len(df.index)))

# Write recipe outputs
added_index = dataiku.Dataset("added_index")
added_index.write_with_schema(df)