import requests
import json
import urllib3
import nexusLib


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Receives an auth token and mgmt address
#Returns a list of interfaces

def getNxIntList(addr,auth_cookie):

    #resourceQuery is derived from DME model through Visore Browser

    resourceQuery = ""
    myheaders = {
      'Content-Type': 'application/json',
      'Cookie': 'APIC-cookie=' + auth_cookie
      }
    payload = []

    url = "https://"+addr+resourceQuery



    response = requests.get(url,data=json.dumps(payload), verify=False,headers=myheaders)
    return response.json()

#Receives an auth token, mgmt address, and nested list returned from getNXIntList
#Returns HTML code
def printNxIntList(addr,auth_cookie,intList):

    #resourceQuery is derived from DME model through Visore Browser

    resourceQuery = ""
    myheaders = {
      'Content-Type': 'application/json',
      'Cookie': 'APIC-cookie=' + auth_cookie
      }
    payload = []

    url = "https://"+addr+resourceQuery
    response = requests.get(url,data=json.dumps(payload), verify=False,headers=myheaders)

    #response without .json() = HTTP Code
    
    return response

def main():

    addr = "10.10.20.40"
    userName = "admin"
    pwd = "RG!_Yw200"

   
    cookie = nexusLib.getCookie(addr,userName,pwd)
if __name__ == '__main__':
    main()

