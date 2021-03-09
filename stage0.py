import requests
from requests.auth import HTTPBasicAuth
import json

from env import config

### MERAKI ###
#url = config['MERAKI_BASE_URL']
url = "https://api.meraki.com/api/v0/organizations"
payload = None

headers= {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": config['MERAKI_KEY']
}

response = requests.request('GET', url, headers=headers, data=payload)

if response.status_code == 200:
    print("Meraki Access verified")
else:
    print(f"Meraki status code: {response.status_code}")


response_txt = response.text.encode('utf8')
response_txt2 = json.loads(response_txt)

#Prints names and organization IDs.
#for org in response_txt2:
#    #print('Name: ', org["name"], ", \t ID: ", org["id"])

for org in response_txt2:
    if org["name"] == 'DevNet Sandbox':
        print(org["id"])
        orgID = org["id"]
      
#print(response.text.encode('utf8'))

organizationId = orgID #549236
#url = "https://api.meraki.com/api/v1/organizations/549236/networks"
url = f'https://api.meraki.com/api/v1/organizations/{organizationId}/networks'
response2 = requests.request('GET', url, headers=headers, data = payload)
#print(response2.text.encode('utf8'))

response_txt = response2.text.encode('utf8')
response_txt2 = json.loads(response_txt)

for org in response_txt2: 
    if org["name"] == "DevNet Sandbox ALWAYS ON":
        orgID2= org["id"]

networkID = orgID2 #L_646829496481105433
#url = "https://api.meraki.com/api/v1/networks/L_646829496481105433/devices"
url = f'https://api.meraki.com/api/v1/networks/{networkID}/devices'
response3 = requests.request('GET', url, headers=headers, data = payload)
response_txt = response3.text.encode('utf8')
response_txt3 = json.loads(response_txt)


# Creating dictionaries    
dict = {"device1":{"model":"MX65", "serial":"Q2QN-9J8L-SLPD", "mac":"e0:55:3d:17:d4:23"},
        "device2":{"model":"MR53", "serial":"Q2MD-BHHS-5FDL", "mac":"88:15:44:60:21:10"},
        "device3":{"model":"MS220-8P","serial":"Q2HP-F5K5-R88R","mac":"88:15:44:df:f3:af"}}

#Creating json file
with open('devices', 'w') as fp:
    json.dump(dict, fp)


