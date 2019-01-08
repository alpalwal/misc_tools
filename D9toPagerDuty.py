'''
Services > Add a service
Set name (d9Events)
Integration type - "Use our API directly" Events APIv2

'''
# service_key = "b517acf9dfb247b6a4b9e348d9ff0b7e"
# api_key = "_qvFdsyjkxsJ7AFxyyLe" 


import json
from botocore.vendored import requests
import os

#Feed in the SNS Topic from an env. variable
service_key = os.getenv('service_key','')
api_key = os.getenv('api_key','')

def lambda_handler(event, context):
    #Pull the Dome9 message out of the SNS message
    raw_message = event['Records'][0]['Sns']['Message']
    message = json.loads(raw_message)


    rule_name = message['rule']['name']
    status = message['status']
    entity_id = message['entity']['id']
    entity_name = message['entity']['name']
    rule_name = message['rule']['name']
    
    if not service_key or not api_key:
        return("Service key or api key not defined. Please set it before running")

    if status == "Passed":
        return ("Previously failing rule has been resolved: {} \n ID: {} \nName: {}. Not opening incident \n".format(rule_name, entity_id, entity_name))

    # Triggers a PagerDuty incident without a previously generated incident key
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={0}'.format(api_key),
        'Content-type': 'application/json',
    }

    payload = json.dumps({
        "service_key": service_key, # Enter service key here
        "event_type": "trigger",
        "description": "Compliance Failure: {0}".format(rule_name),
        "details": message
    })

    r = requests.post('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                      headers=headers,
                      data=payload,
    )

# TO FIX:
# 403
# {"status":"throttle exceeded","message":"Requests for this service are arriving too quickly. Please retry later."}

    print (r.status_code)
    print (r.text)
    return r.text
