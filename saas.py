#!/usr/bin/python

import os,commands,time,sys

print "Plzzz wait for the software application list......list is upto the mark!!!!!!"
time.sleep(2)
x="""             
print "press 1 to access firefox:"
print "press 2 to access text editor:"
print "press 3 to access vlc:"
pint "press  4 to access office:"
print "press 5 to access webcam:"
"""
print x
get_software=raw_input()

if  get_software == '1':
	os.system('ssh -X shalini@192.168.10.174 firefox')


elif  get_software == '2':
	os.system('ssh -X shalini@192.168.10.174 gedit')

elif  get_software == '3':
	os.system('ssh -X shalini@192.168.10.174 vlc')

elif  get_software == '4':
	os.system('ssh -X  shalini@192.168.10.174 office')

elif  get_software == '5':
	os.system('ssh -X shalini@192.168.10.174 webcam')
else:
	print "wrong choice"
	execfile('list.py')

