#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
from socket import *
from time import *
from sys import *
from asyncore import *
import sys,time,socket,asyncore
#Définir un serveur
#il droit attendre la connexion d'un client
#module socket contient les fonctions et les classes
URL = '127.0.0.1'
Port = 400
#Création de la socket coté serveur
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#lier la socket avec l'adresse précise
#try:
mySocket.bind((URL,Port))
#except socket.error:
#	print"la Liaison échoué."
#	sys.exit()

while 1:
		print "serveur prêt, en attente de requête .."
		mySocket.listen(5) #recevoir les requete envoyé par le client avec 5 nombre maximale de conx
		#connexion établie
		connexion, adresse = mySocket.accept()
		print "client connecté  "
		print"L'adresse",adresse,"vient de se connecter au serveur !"
		connexion.send("Vous ête connecté")
		msgClient = connexion.recv(1024)
		while 1:
			print"Clt>", msgClient
			if msgClient.upper() == "FIN":
					break
			msgServeur = raw_input("Ser> ")
			connexion.send(msgServeur)
			msgClient = connexion.recv(1024)
		connexion.send("Au revoir!")
		print"connexion interrompue."
		connexion.close()

		ch = raw_input("<R>ecommencer <T>erminer ?")
		if ch.upper() == 'T' :
			break
		print"connexion interrompue"