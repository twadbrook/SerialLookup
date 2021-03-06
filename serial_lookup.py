#!/usr/bin/python

#script
import subprocess
import plistlib
import csv
import urllib2


print "Waiting for network access..."
cmd = ['/usr/sbin/scutil', '-w', 'State:/Network/Global/DNS', '-t', '180']
proc = subprocess.Popen(cmd, shell=False, bufsize=-1,
						stdin=subprocess.PIPE,
						stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(output, dummy_error) = proc.communicate()


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

try:
	response = urllib2.urlopen('http://10.4.10.1/serials.csv', timeout=120)
except URLError as e:
	prnt "ERROR: Could not reach 10.4.10.1 after 120 seconds: %s" % e
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
