# This file is the actual code for the custom Jython step add-record-id

start_index_at_1 = step_config.get["start_index_at_1"]

# Define here a function that returns the result of the step.
count = 0
def process(row):
    start_index_at_1 = params.get('start_index_at_1')
    global record_id
    
    record_id = count
    if start_index_at_1:
        record_id +=1
    count +=1  
    return record_id
