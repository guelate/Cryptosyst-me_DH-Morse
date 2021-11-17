import socket
import select 

serveur = socket.socket()
host,port = "127.0.0.1",8000
serveur.bind((host,port)) 
serveur.listen() 
client_connecte = True
serveurliste = [serveur] #liste serveurs

# Lancement du serveur 

while client_connecte:

	connexion1, connexionE, connexionS = select.select(serveurliste, [],serveurliste)

	for socketo in connexion1:

		if socketo is serveur:

			client,adresse = serveur.accept() 
			print("Vous êtes connecté au serveur.")
			serveurliste.append(client)

		else:
			
			data = socketo.recv(128).decode("utf-8")
			
			if data:
				print(data)

			else:
				
				serveurliste.remove(socketo)
				print("Vous êtes déconnecté du serveur .")
				break


