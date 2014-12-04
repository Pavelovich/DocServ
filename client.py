#!/usr/bin/python
import socket
import os

print '''

------------------------------------------------------------------------------
    ____             _____
   / __ \____  _____/ ___/___  ______   __
  / / / / __ \/ ___/\__ \/ _ \/ ___/ | / /
 / /_/ / /_/ / /__ ___/ /  __/ /   | |/ /
/_____/\____/\___//____/\___/_/    |___/

DocServ client version 1.1.0

Copyright (c) 2014 Sasha Pavelovich
MIT license

Commands:           ------------>
In the URL prompt,

>exit   - Quit the program
>new    - Enter a new hostname

'''
hostname = str(socket.gethostname())
username = str(os.getenv("LOGNAME"))
host = raw_input("DocServ > hostname: ")

while 1:
    request = raw_input("DocServ > tdtp://"+host+"/")
    if request == ">exit":
        print "------------------------------------------------------------------------------"
        print ''
        exit()
    elif request == ">new":
        host = raw_input("DocServ > hostname: ")
    elif request == '':
        request = '/'
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,32891))
    s.send(''+username+'|'+hostname+'|'+request)
    print s.recv(1024)
    s.close()
