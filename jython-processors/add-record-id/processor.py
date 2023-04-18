# This file is the actual code for the custom Jython step add-record-id

count = 0
def process(row):
    global count
    record_id = count
    if params.get('start_index_at_1'):
        record_id +=1
    count +=1  
    return record_id
