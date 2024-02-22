import csv
from filler import submit_internship_entry
import time

def submit_entries_from_file(file_path):
    results = [] 

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            applicationId = row['applicationId']
            Date__c = row['Date']
            Start_Time__c = row['Start time']
            End_Time__c = row['End time']
            Description__c = row['Description']
            result = submit_internship_entry(applicationId, Date__c, Start_Time__c, End_Time__c, Description__c)
            print(applicationId, Date__c, Start_Time__c, End_Time__c, Description__c, ' - ', result)
            time.sleep(10)
    return results

file_path = 'data2.csv'  
results = submit_entries_from_file(file_path)
