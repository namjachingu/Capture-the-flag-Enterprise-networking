import requests
import json
from requests.auth import HTTPBasicAuth
from env import config
from dnac_config import DNAC_IP, USERNAME, PASSWORD

requests.packages.urllib3.disable_warnings()

def get_auth_token():
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    response = requests.post(url, auth=HTTPBasicAuth(config['DNAC_USER'], config['DNAC_PASSWORD'])) 
    token = response.json()['Token']    
    print("Token Retrieved: {}".format(token))  
    return token 

def get_device_list():
    token = get_auth_token()
    url = "https://sandboxdnac.cisco.com/api/v1/network-device" 
    header = {'x-auth-token': token, 'content-type' : 'application/json'} 
    response = requests.get(url, headers=header)  
    device_list = response.json() #capture the data from the controller
    #print(device_list)
    for org in device_list:
        print("type: ", org['type'], " \nmacAddress: ", org['macAddress'], "\nserialNumber: ", org['serialNumber'])



'''
macAddress
serialNumber
hostname
'''

if __name__ == "__main__":
  get_auth_token()
  get_device_list()
