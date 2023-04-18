# Code for custom code recipe transpose (imported from a Python recipe)
import dataiku
import pandas as pd, numpy as np

# Import the helpers for custom recipes
from dataiku.customrecipe import get_input_names_for_role
from dataiku.customrecipe import get_output_names_for_role
from dataiku.customrecipe import get_recipe_config

# Fetch input & output dataset
input_dataset_name = get_input_names_for_role('input_dataset')[0]
input_dataset = dataiku.Dataset(input_dataset_name)

# For outputs, the process is the same:
output_dataset_name = get_output_names_for_role('output_dataset')[0]
output_dataset = dataiku.Dataset(output_dataset_name)

# Fetch input parameters
transpose_col = get_recipe_config()['column_name']

# Transpose dataset
df = input_dataset.get_dataframe()
df = df.set_index(transpose_col)
transpose_df = df.transpose() 
transpose_df.insert(0, transpose_col, transpose_df.index)

# Write recipe outputs
output_dataset.write_with_schema(transpose_df)