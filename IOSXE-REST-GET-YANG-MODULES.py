import requests

addr = "10.10.20.48"

url = "https://"+addr+":443/restconf/data/ietf-yang-library:modules-state"


username = 'developer'
password = 'C1sco12345'
payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm'
}

response = requests.request("GET", url, auth = (username,password), verify = False, headers=headers, data=payload)

print(response.text)
