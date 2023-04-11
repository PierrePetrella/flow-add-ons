
import dataiku

from dataiku.customrecipe import get_input_names_for_role
from dataiku.customrecipe import get_output_names_for_role
from dataiku.customrecipe import get_recipe_config



input_dataset_name = get_input_names_for_role('input_dataset')[0]
input_dataset = dataiku.Dataset(input_dataset_name)

# For outputs, the process is the same:
output_dataset_name = get_output_names_for_role('main_output')[0]
output_dataset = dataiku.Dataset(output_dataset_name)

#my_variable = get_recipe_config()['parameter_name']


# Note about typing:
# The configuration of the recipe is passed through a JSON object
# As such, INT parameters of the recipe are received in the get_recipe_config() dict as a Python float.
# If you absolutely require a Python int, use int(get_recipe_config()["my_int_param"])


#############################
# Your original recipe
#############################

import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
empty_dataset = dataiku.Dataset("ecommerce_transactions")
df = empty_dataset.get_dataframe()

output_df = df.dropna(axis=1, how='all', inplace=False)

# Write recipe outputs
output = dataiku.Dataset("removed_empty_rows")
output.write_with_schema(output_df) 