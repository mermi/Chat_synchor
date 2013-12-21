#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
from socket import *
from time import *
from asyncore import *
from sys import *
import sys,time,socket,asyncore
#Coté client
#client dialogue avec un serveur ad hoc
URL = '127.0.0.1'
Port = 400
#créer une socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#envoie d'une requête de connexion
#try:
mySocket.connect((URL,Port))
#except socket.error:
#	print "La connexion a échoué."
#	sys.exit()

print"Connexion établie avec le serveur."

#dialogue avec le serveur
msgServeur = mySocket.recv(1024)

while 1:
	if msgServeur.upper() == "FIN":
		break
	print"Serv>", msgServeur
	msgClient = raw_input ("Clt>")
	mySocket.send(msgClient)
	msgServeur = mySocket.recv(1024)
#fermeture de connexion

print"connexion interrompue"
mySocket.close()