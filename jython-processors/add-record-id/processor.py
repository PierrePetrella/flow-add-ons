# This file is the actual code for the custom Jython step add-record-id


# Define here a function that returns the result of the step.
count = 0
def process(row):
    start_index_at_1 = int(params.get('start_index_at_1'))
    global count
    record_id = count
    if start_index_at_1:
        record_id +=1
    count +=1  
    return record_id
    return 3
