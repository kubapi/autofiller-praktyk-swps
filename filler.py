import requests
import json

def submit_internship_entry(applicationId, Date__c, Start_Time__c, End_Time__c, Description__c):
    headers = {
        'authority': 'myuniversity.swps.edu.pl',
        'accept': '*/*',
        'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://myuniversity.swps.edu.pl',
    }
    
    message_payload = {
        "actions": [{
            "id": "85;a",
            "descriptor": "aura://ApexActionController/ACTION$execute",
            "callingDescriptor": "UNKNOWN",
            "params": {
                "namespace": "",
                "classname": "MySwpsInternshipReportController",
                "method": "upsertEntry",
                "params": {
                    "applicationId": applicationId,
                    "entryToUpsert": {
                        "Date__c": Date__c,
                        "Start_Time__c": Start_Time__c,
                        "End_Time__c": End_Time__c,
                        "Description__c": Description__c,
                        "Career_Services_Application__c": applicationId
                    }
                },
                "cacheable": False,
                "isContinuation": False
            }
        }]
    }
    
    data = {
        "message": json.dumps(message_payload),
        "aura.context": '{"mode":"PROD","fwuid":"YWYyQV90T3g3VDhySzNWUm1kcF9WUVY4bi1LdGdMbklVbHlMdER1eVVlUGcyNDYuMTUuNS0zLjAuNA","app":"siteforce:communityApp","loaded":{"APPLICATION@markup://siteforce:communityApp":"xUUH_isHmNQqCOJ9yNTV7A","COMPONENT@markup://instrumentation:o11ySecondaryLoader":"iVoI_RYCX4m4O5loBTnQfA"},"dn":[],"globals":{},"uad":false}',
        "aura.token": "",
    }

    response = requests.post(
        "https://myuniversity.swps.edu.pl/s/sfsites/aura",
        headers=headers,
        data=data,
    )
    
    text_response = json.loads(response.text)
    
 
    if response.status_code == 200 and text_response['actions'][0]['state'] != 'ERROR':
        return "🍀 Entry submitted successfully."
    else:
        return f"👹 Failed to submit entry."