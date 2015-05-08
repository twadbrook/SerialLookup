#!/usr/bin/python

#script
import subprocess
import plistlib
import csv
import urllib2

def get_hardware_info():
    '''Uses system profiler to get hardware info for this machine'''
    cmd = ['/usr/sbin/system_profiler', 'SPHardwareDataType', '-xml']
    proc = subprocess.Popen(cmd, shell=False, bufsize=-1,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, dummy_error) = proc.communicate()
    try:
        plist = plistlib.readPlistFromString(output)
        # system_profiler xml is an array
        sp_dict = plist[0]
        items = sp_dict['_items']
        sp_hardware_dict = items[0]
        return sp_hardware_dict
    except BaseException:
        return {}
        
def change_local_hostname(hostname):
    cmd = ['/usr/sbin/scutil', '--set', 'LocalHostName', hostname]
    proc = subprocess.Popen(cmd, shell=False, bufsize=-1,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, dummy_error) = proc.communicate()

def change_hostname(hostname):
    cmd = ['/usr/sbin/scutil', '--set', 'HostName', hostname]
#    cmd = ['/usr/sbin/scutil', '--set', 'HostName', hostname + ".milken.us"]
    proc = subprocess.Popen(cmd, shell=False, bufsize=-1,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, dummy_error) = proc.communicate()

def change_computername(hostname):
    cmd = ['/usr/sbin/scutil', '--set', 'ComputerName', hostname]
    proc = subprocess.Popen(cmd, shell=False, bufsize=-1,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, dummy_error) = proc.communicate()


response = urllib2.urlopen('http://hs-mds-01.milken.us/serials.csv')
html = response.read()
output = open('serials.csv', 'wb')
output.write(html)
output.close()

with open('serials.csv', mode='r') as infile:
    reader = csv.reader(infile)
    keyDict = dict(reader)

hardware_info = get_hardware_info()
mySerialNumber = hardware_info.get('serial_number', 'UNKNOWN')
myHostName = keyDict[mySerialNumber]

change_local_hostname(myHostName)
change_hostname(myHostName)
change_computername(myHostName)
