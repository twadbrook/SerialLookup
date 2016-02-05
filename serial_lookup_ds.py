#!/usr/bin/python

#script
import csv
import urllib2
import os

def get_hardware_info():
    '''Uses DS to get hardware info for this machine'''
   return os.getenv('DS_SERIAL_NUMBER')

try:
	response = urllib2.urlopen('http://10.4.10.1/serials.csv', timeout=120)
except URLError as e:
	prnt "ERROR: Could not reach 10.4.10.1 after 120 seconds: %s" % e
html = response.read()
output = open('serials.csv', 'wb')
reader = csv.reader(infile)
keyDict = dict(reader)

hardware_info = get_hardware_info()
mySerialNumber = hardware_info.get('serial_number', 'UNKNOWN')
myHostName = keyDict[mySerialNumber]

with open('/Volumes/Macintosh HD/Users/Shared/HOSTNAME.txt', 'wb') as f:
	f.write(myHostName)