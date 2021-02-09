# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:56:57 2021

@author: Gabo
"""
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?";
#orig = "Quito"
#dest = "Guayaquil"
key = "GrDV1wtc2AbnADV9XWqPMyBmeVbsIVWo"
while True:
    orig = input("Starting location: ")
    dest = input("Destination: ")
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
print("URL: " + (url))
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    
