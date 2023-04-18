# This file is the actual code for the custom Jython step add-record-id


# Define here a function that returns the result of the step.
if params.get('start_index_at_1'):
    record_id = 0
else:
    record_id = -1

def process(row):
    global record_id
    record_id =+1
    
    
    return record_id
