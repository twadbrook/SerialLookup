#!/usr/bin/python

#script
import csv
import urllib2
import os

def get_hardware_info():
    '''Uses DS to get hardware info for this machine'''
    return os.getenv('DS_SERIAL_NUMBER')

with open('/tmp/DSNetworkRepository/Files/serials.csv', 'rb') as infile:
    reader = csv.reader(infile)
    keyDict = dict(reader)

hardware_info = get_hardware_info()
myHostName = keyDict[hardware_info]

with open('/Volumes/Macintosh HD/Users/Shared/HOSTNAME.txt', 'wb') as f:
    f.write(myHostName)
    f.write('\n')

