import PySimpleGUI as sg  #pip install PySimpleGUI and sudo apt-get install python3-tk

# When a light button is pushed and the confirmation that the primitive is successful
# the icon will be changed. These imports support that functionality.
import os.path
import PIL.Image #pip install Pillow
import io
import base64
import urllib.parse
from rdflib import Graph

# for reading configuration parameters from file
import argparse
from configparser import ConfigParser

# for sending http requests using json
import requests
from json import loads, dumps

# the sensors and http listener (for notifications) use threads
import threading
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

appIP = '127.0.0.1 '
appPort = '8080'
appID = 'CAdmin'
cseIP = '3.136.39.208'
csePort = '8080'
cseID = 'capstone-iot'
cseName = 'cse-in'
originator = appID
def createAE(resourceName):
    poa = 'http://{}:{}'.format(appIP,appPort)
    payld = { "m2m:ae": { "rr": True, "api": "NR_AE001", "apn": "IOTApp", "csz": [ "application/json" ], "srv": [ "2a" ], "rn": resourceName, "poa": [ '123s' ],"acpi": ["capstone-iot"] } }
    
    print ("AE Create Request")
    #print (payld)
    url = 'http://' + cseIP + ':' + csePort + '/' + cseID
    hdrs = {'X-M2M-RI':"CAE_Test",'X-M2M-Origin':originator, 'X-M2M-RVI':'2a' ,'Content-Type':"application/json;ty=2"}
    r = requests.post(url, data=dumps(payld), headers=hdrs)
    print ("AE Create Response")
    print (r.text)

    return getResId('m2m:ae',r)
  
def getResId(tag,r):
    try:
        resId = r.json()[tag]['ri']
    except:
        #allready created
        resId = ""
    return resId
def createSubscription(resourceName, parentID):
    payld = { "m2m:sub": { "rn": resourceName, "enc": {"net":[3]}, "nu":[originator],"acpi": ["cse-in/bruh"]} }
    print ("Sub Create Request")
    #print (payld)
    url = 'http://' + cseIP + ':' + csePort + '/' + parentID
    hdrs = {'X-M2M-RI':"Sub",'X-M2M-Origin':originator, 'X-M2M-RVI':'2a' ,'Content-Type':"application/json;ty=23"}
    r = requests.post(url, data=dumps(payld), headers=hdrs)
    print ("SUB Create Response")
    print (r.text)

    return getResId('m2m:sub',r)


createSubscription("bruh_subscriber","cse-in")