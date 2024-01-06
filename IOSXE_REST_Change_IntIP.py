import requests
import json
import iosXeLib

# These values should be updated based on the device
ip_addr = '10.10.20.48'
username = "developer"
pw = "C1sco12345'

int_list = iosXeLib.getInts(deviceIP,username,pw) #Gets list of interfaces and IP addresses

iosXeLib.printInt(int_list) #This iterates the dictionary that is returned

#Gets interface to modify and validates

valid_int = True

while valid_int ==True:
    valid_int = False
    #Don't modify G1. It's the management interface
    int_Name = input("Which interface do you want to modify?")

    #local function to check int name is valid
    #Takes interface list and userinput and returns boolean
    #True if interface name is in the list

    valid_int = validate_int(int_list,int_name)
    if valid_int == False:
        print("Bad interface name")

#Gets and validates IP address /mask

valid_IP = True
while valid_IP == True:
    int_IP = input("Enter a new IP address for " + int_name + ":")
    valid_IP = isValidIP(int_IP)
    if valid_IP == False:
        print("IP must be x.x.x.x where x >=0 and x <=255")

valid_mask = True
while valid_mask == True:
    int_mask = input("Enter a new mask for " + int_name + " with IP of " + int_IP + ":")
    valid_mask = isValidMask(int_mask)
    if valid_mask == False:
        print("Bad Mask")
        
#Updates interface with new address and mask

httpCode = iosXeLib.update_iosXE_Int(ip_addr,username,pw,int_name,int_ip,int_mask)

#Error Processing

if str(httpCode) == "<Response [200]>":
    int_list = iosXeLib.getInts(deviceIP,username,pw) #Gets list of interfaces and IP addresses

    iosXeLib.printInt(int_list) #This iterates the dictionary that is returned
else:
    print("Update Failed! No change.") #Bonus 5 points for printing the error code


    

    
