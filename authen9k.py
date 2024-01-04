import requests

def getCookie(addr,name, pwd) :

#NX REST API Authen See REST API Reference for format of payload below

    url = "https://"+ addr + "/api/aaaLogin.json"
 
    payload= {"aaaUser" :
              {"attributes" :
                   {"name" : name,
                    "pwd" : pwd}
               }
          }

    response = requests.post(url, json=payload, verify = False)
    
    return response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]


#Main



#Get Session Cookie for NX switch. Change address below as needed

#address = '10.10.20.177'
address = "10.10.20.40"
user = "admin"
passw = "RG!_Yw200"

#Use the cookie below to pass in request. Cookie is good for 600 seconds

cookie = getCookie(address,user,passw)
print(cookie)



