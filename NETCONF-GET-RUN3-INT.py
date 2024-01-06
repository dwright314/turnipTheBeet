## ********************************************
##                                            *
##  Gets Cisco Native Interfaces              *
##                                            *
## ********************************************


import xml.etree.ElementTree as ET
import xmltodict
import xml.dom.minidom
from lxml import etree
from ncclient import manager
from collections import OrderedDict

#router = {"host": "10.10.20.175", "port" : "830",
          #"username":"cisco","password":"cisco"}

router = {"host": "10.10.20.48", "port" : "830",
          "username":"developer","password":"C1sco12345"}

##<filter>
##    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
##        <interface>
##            
##        </interface>
##    </interfaces>
##</filter>"""

netconf_filter = """
<filter
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <native
        xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  
            <interface>
            
            </interface>
        </native>
</filter>"""


with manager.connect(host=router['host'],port=router['port'],username=router['username'],password=router['password'],hostkey_verify=False) as m:

    netconf_reply = m.get_config(source = 'running', filter = netconf_filter)

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

print("#" * 40)

#Parse returned XML to Dictionary

netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

print(netconf_data)

print("d" *40)

#Create List of Interfaces

interfaces = netconf_data["native"]["interface"]

print(interfaces)

print("I" * 40)

for interface in interfaces:
    print(interfaces[interface])
    print()      
