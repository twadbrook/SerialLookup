#!/usr/bin/python

import os
import subprocess

def change_local_hostname(hostname):
    cmd = ['/usr/sbin/scutil', '--set', 'LocalHostName', hostname]
    proc = subprocess.Popen(cmd, shell=False, bufsize=-1,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, dummy_error) = proc.communicate()

def change_hostname(hostname):
    cmd = ['/usr/sbin/scutil', '--set', 'HostName', hostname]
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


if os.path.exists('/Users/Shared/HOSTNAME.txt'):
	with open ('/Users/Shared/HOSTNAME.txt', 'rb') as f:
		hostname = str(f.read()).strip()
		change_local_hostname(hostname)
		change_hostname(hostname)
		change_computername(hostname)