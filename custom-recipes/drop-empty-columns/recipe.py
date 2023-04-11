
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

from dataiku.customrecipe import get_input_names_for_role
from dataiku.customrecipe import get_output_names_for_role
from dataiku.customrecipe import get_recipe_config



input_dataset_name = get_input_names_for_role('input_dataset')[0]
input_dataset = dataiku.Dataset(input_dataset_name)

# For outputs, the process is the same:
output_dataset_name = get_output_names_for_role('output_dataset')[0]
output_dataset = dataiku.Dataset(output_dataset_name)

#my_variable = get_recipe_config()['parameter_name']
#my_variable = get_recipe_config().get('parameter_name', None)


# Read recipe inputs
df = input_dataset.get_dataframe()

output_df = df.dropna(axis=1, how='all', inplace=False)

# Write recipe outputs
output_dataset.write_with_schema(output_df) 