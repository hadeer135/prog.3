# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:40:10 2024

@author: hadeer dowidar
### socket programming 

"""

from socket import*
s=socket(AF_INET , SOCK_STREAM)
print ("HAEEEEEERR")
### created a socket --> done 

host ='127.0.0.1' ### here (is standard address of loopback) ip address and it also can be an empty string passed 
port = 40674
### first bind then listen 
s.bind(host,port) ### bindded to the port given 
print("socket bindded to the port")
s.listen(5)  ### the number "5" --> backlog means accept to 5 connections and kept waiting but if 6 or more it is refused 
print(" socket is listening ")

### after listen accept --> connection started 

while True :
    c,address =s.accept()
    print ("we are getting connection from ",address) ##--> connecton with the client 
    
    c.send(b'connection establishing is done ') ## sent to the client 
    c.close() ## close connection with the client 
    
    
    

