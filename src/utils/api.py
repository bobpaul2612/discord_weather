import json 

def generator_response(status_code, msg, data=None):
    '''
    A util to generate response for lambda
    '''
    
    if not data:
        data = {}

    body_msg = {
        "info": msg,
        "data": data
    }

    return {
        "statusCode": status_code,
        "body": json.dumps(body_msg)
    }
    
