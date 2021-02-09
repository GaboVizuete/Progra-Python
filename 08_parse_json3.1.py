# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:32:22 2021

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
    if orig == "quit" or orig == "q":
        break
    
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    print("Direction from " + (orig) + " to "+(dest))
    print("Trip Duration:   " + (json_data["route"]["formattedTime"])) 
    print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61))) 
    print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])**3.78))) 
    print("==========================================")
    for each in jason_data["route"]["Legs"][0]["maneuvers"]:
        