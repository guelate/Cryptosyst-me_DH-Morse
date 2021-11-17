import cryptocode
import random
import socket 

phrase ="Bonjour tout le monde , la partie va commencer c'est partie ."
clé = 0
entrer = None
liste_Min = []
liste_apostrophe = []
phrase_apostropheNul = ""

client_serveur = socket.socket()
host,port = "127.0.0.1",8000

# Fonction Deffie-Hellman 

def DH(x,y):

	global clé
	Nbpremier,G = 53,5
	a = random.randrange(x)
	b = random.randrange(y)
	
	A = pow(G,a,Nbpremier)
	B = pow(G,b,Nbpremier)
	
	if(pow(B,a,Nbpremier) == pow(A,b,Nbpremier)):

		clé = pow(B,a,Nbpremier)
		clé = pow(B,a,Nbpremier)
		src = open("fichier"+".clé","w")
		src.write("La clé du serveur est : "+str(clé))
		src.close()
			
	else:

		return 


       




# Dictionnaire alphabet Morse

Alphabet_Morse = { 'A':'.-', 'a':'.-', 'B':'-...', 'b':'-...',

					'C':'-.-.', 'c':'-.-.', 'D':'-..', 'd':'-..', 'E':'.','e':'.',

					'F':'..-.', 'f':'..-.', 'G':'--.', 'g':'--.', 'H':'....','h':'....',

					'I':'..', 'i':'..', 'J':'.---', 'j':'.---' ,'K':'-.-','k':'-.-',

					'L':'.-..','l':'.-..', 'M':'--', 'm':'--','N':'-.','n':'-.',

					'O':'---', 'o':'---','P':'.--.', 'p':'.--.','Q':'--.-','q':'--.-',

					'R':'.-.','r':'.-.', 'S':'...', 's':'...','T':'-','t':'-',

					'U':'..-','u':'..-' ,'V':'...-', 'v':'...-','W':'.--','w':'.--',

					'X':'-..-','x':'-..-' ,'Y':'-.--', 'y':'-.--','Z':'--..','z':'--..',

					'1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....',
					
					'6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----',
					
					',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',

					'(':'-.--.', ')':'-.--.-' ,'!':'-.-.-----.',':':'---...', ';': '-.-.-.', 

				}

#fonction de cryptage en morse

def cryptage(message):

	chiffré = ''

	for letter in message:

		if letter != ' ':

			chiffré += Alphabet_Morse[letter] + ' '

		else:

			chiffré += ' '

	return chiffré


# Fonction décryptage morse 

def décryptage(message):

	message += ' ' 
	déchiffré = ''
	citext = ''

	for letter in message:

		if (letter != ' '): 

			i = 0
			citext += letter

		else:

			i += 1

			if i == 2 :

				déchiffré += ' '
			else:

				déchiffré += list(Alphabet_Morse.keys())[list(Alphabet_Morse
				.values()).index(citext)]
				citext = ''

	return déchiffré


# algo main cryptage/décryptage avec encodage et décodage 

def main_algo(texte):

	global liste_Min
	global liste_apostrophe
	global phrase_apostropheNul

	src = open("fichier"+".enc","w")

	msg = cryptage(texte) 
	verif1 = msg
	print("\nL'alphabet de la phrase est encodé:",msg)
	msg = décryptage(msg)
	verif2 = msg

	msg = cryptocode.encrypt(msg,str(clé))
	src.write(msg)
	src.close()
	msg1 = cryptocode.decrypt(msg,str(clé)) 
	print("\nEntrer le méssage chiffrer qui est dans le fichier: fichier.enc\n")
	x = input()
	if (x == msg):
		print("\nL'alphabet de la phrase est décodé : ",msg1)
		for v in liste_apostrophe:
			phrase_apostropheNul = phrase_apostropheNul[:v]+"'"+phrase_apostropheNul[v:]

		verification(verif1,verif2)
		print("\nOn retrouve donc la phrase :",phrase_apostropheNul)


	else:
		print("\nLe méssage chiffré est mauvais")

# Fonction vérification cryptage morse 
def verification(x,y):

	if(décryptage(x) == y):

		print("\nLa vérification est bonne")

	else:

		print("\nL'encodement et le décodement ne ce corresponde pas .")



def authentification():
	
	global entrer
	entrer = input("Entrer la clé du serveur : ") 


def main():

	global liste_Min
	global phrase
	global phrase_apostropheNul
	global liste_apostrophe
	liste_caractereNull = ""
	
	i = 0
	y = 0

	print("\nLa phrase à coder et decoder est :",phrase)

	#extraction minuscule , apostrophe 

	for v in phrase:
		
		if(v.islower()):
			liste_Min.append(i)
		i += 1
		
		if(v != "'"):
			phrase_apostropheNul += v
			
		else:
		
			liste_apostrophe.append(y)

		y += 1

	main_algo(phrase_apostropheNul)
	
	
#lancement main()

if __name__ == "__main__":

	DH(50,25)
	authentification()

	while True :

		if (str(entrer) == str(clé)):
			client_serveur.connect((host,port))
			main()
			break


