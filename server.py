#!/usr/bin/python
import socket
import os

#Enter the path to the server root directory
path = "srv/"
#Enter the path to the log file
log = "log/"
#Enter the IP address to listen on
listen = "127.0.0.1"

print '''

------------------------------------------------------------------------------
    ____             _____
   / __ \____  _____/ ___/___  ______   __
  / / / / __ \/ ___/\__ \/ _ \/ ___/ | / /
 / /_/ / /_/ / /__ ___/ /  __/ /   | |/ /
/_____/\____/\___//____/\___/_/    |___/

DocServ server version 1.1.0

Copyright (c) 2014 Sasha Pavelovich
MIT license

'''

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((listen,32891))
s.listen(5)
while 1:
    client, address = s.accept()
    data = client.recv(1024)
    if data:
        ip,port = client.getpeername()
        data = data.split('|')
        username = data[0]
        hostname = data[1]
        data = data[2]
        request = ""+ip+" "+username+" @ "+hostname+" - "+data
        print request
        if log.endswith('/'):
            log = log[:-1]
        with open(log+"/server.log",'a') as f:
            f.write(request+'\n')
        if path not in os.path.abspath(data):
            client.send("File path error")
        if data == '/':
            if os.path.isfile(path+"/index.txt") == False:
                client.send("File not found")
                continue
            file = open(path+"/index.txt", 'r')
            text = file.read()
            client.send(text)
            file.close()
            continue
        if path.endswith('/'):
            path = path[:-1]
        if os.path.exists(path+'/'+data) == False:
            client.send("File not found")
            continue
        elif os.path.isfile(path+'/'+data) == False:
            if data.endswith('/'):
                data = data[:-1]
            if os.path.isfile(path+'/'+data+"/index.txt") == False:
                client.send("File not found")
                continue
            file = open(path+'/'+data+"/index.txt", 'r')
            text = file.read()
            client.send(text)
            file.close()
            continue
        file = open(path+'/'+data, 'r')
        text = file.read()
        client.send(text)
        file.close()
    client.close()
