from random import randint
import math
import time

# ------------- Fonction qui retourne vrai si l'input est un nb premier
def estPremier(nb):
	flag=1
	i=1

	while i<nb:
		if(nb%i)==0 and i!=1 and i!=nb:
			#print("Nombre non premier !\n")
			flag=0
		i=i+1
	if flag==1:
		#print("Nombre premier !\n")
		return True
	else:
		return False
#estPremier(50)



# ------------- Fonction qui retourne vrai si deux nombres sont premiers entre eux
def sontPremiersEntreEux(a,b):
	c=a
	d=b	
	while(b!=0):
		r=a%b
		a,b=b,r
	if(a==1):
		#print(str(c)+ ' et '+ str(d)+ ' sont premiers entre eux car leur PGCD vaut '+str(a))
		return True	
	else:
		#print("Le PGCD de "+str(c)+ ' et '+ str(d)+" vaut "+str(a))
		return False	
#sontPremiersEntreEux(147,73)	



# ------------- Fonction qui cherche un nombre premier aléatoirement jusqu'au max
def trouvePremier(max):
	a=randint(2,max)
	#si le nombre est pair, on fait +1 pour augmenter le nb de chance qu'il soit premier
	if(a%2==0):
		a=a+1
	if(estPremier(a)==True):
		print(str(a)+" est premier")
		return a
	else:
		trouvePremier(max)
	
#trouvePremier(1500000)

# ------------- Fonction qui cherche l'inverse de b dans Z/modZ
def calculeInverse(b, mod):
	i=1
	while i<mod:
		if((b*i)%mod==1):
			#print("L'inverse de "+str(b)+" vaut "+str(i))	
			return int(i)
		i=i+1
#calculeInverse(4,7)		

#-------------- Utilisation du théorème de Bezout pour l'algo d'Euclide étendu
def bezout(a, b):
	if a == 0 and b == 0: 
		return (0, 0, 0)
	if b == 0: 
		return (a/abs(a), 0, abs(a))
	(u, v, p) = bezout(b, a%b)
	return (v, (u - v*(a//b)), (p))
 
 #------------- Fonction qui calcule l'inverse via l'aglo d'Euclide étendu
def inv_modulo(x, m):
	(u, _, p) = bezout(x, m)
	if p == 1: 
		return int(u%abs(m))
	else: 
		raise Exception("%s et %s ne sont pas premiers entre eux" % (x, m))
#-------------------------------------------------------------------------------

#------------- Fonction qui initialise notre dictionnaire de codage, du caractère ASCII 32 jusqu'au 215
def initialiseCodageAlphabet():
	codageAlphabet={}
	x=1
	for i in range(32,215):
		while not(sontPremiersEntreEux(x,n)):
			x+=1

		codageAlphabet[chr(i)]=x
		x+=1
	return codageAlphabet


#------------ Fonction pour décoder notre message déchiffré
def decodageAlphabet(j):
	for i in codageAlphabet.keys():
		if codageAlphabet[i]==j:
			return i


#------------ Fonction pour obtenir le codage d'un caractère dans notre dictionnaire
def entierLettre(lettre):
	return codageAlphabet[lettre]


#------------- Fonction qui calcul a^b%mod utile pour chiffrer et déchiffrer
def aPuisBModuloN(a,b,mod):
	return pow(a,b)%mod

#------------- Fonction avec exponentiation modulaire
def aPuisBModuloNexpo(a,b,mod):
	result = 1
	while b>0:
		if b&1>0:
			result = (result*a)%mod
		b >>= 1
		a = (a*a)%mod    
	return result

#------------- Fonction pour chiffrer le message avec exponentiation modulaire
def chiffreExpo(message):
        longueurChaine=len(message)
        msgChiffre=[]
        for i in range (0,(longueurChaine)):
                entLettre=entierLettre(message[i])
                lettreChiffre=aPuisBModuloNexpo(entLettre,e,n)
                msgChiffre.append(lettreChiffre)
        return msgChiffre


#------------- Fonction pour chiffrer le message
def chiffre(message):
	longueurChaine=len(message)
	msgChiffre=[]
	for i in range (0,(longueurChaine)):
		entLettre=entierLettre(message[i])
		lettreChiffre=aPuisBModuloN(entLettre,e,n)
		msgChiffre.append(lettreChiffre)
	return msgChiffre


#-------------Fonction pour déchiffrer le message
def dechiffre(msgChiffre):
	longueurChaine=len(msgChiffre)
	msgDechiffre=[]
	for i in range (0,(longueurChaine)):
		chiffreLettre=msgChiffre[i]
		lettreDechiffre=aPuisBModuloN(chiffreLettre,d,n)
		msgDechiffre.append(decodageAlphabet(lettreDechiffre))
		
	return ''.join(msgDechiffre)		

#-------------Fonction pour déchiffrer le message avec exponentiation modulaire
def dechiffreExpo(msgChiffre):
	longueurChaine=len(msgChiffre)
	msgDechiffre=[]
	for i in range (0,(longueurChaine)):
		chiffreLettre=msgChiffre[i]
		lettreDechiffre=aPuisBModuloNexpo(chiffreLettre,d,n)
		msgDechiffre.append(decodageAlphabet(lettreDechiffre))
	return ''.join(msgDechiffre)


#############
##Programme##
#############

#On demande à l'utilisateur d'entrer p et q
verif=False
while verif != True :
	p=int(input("Entrez le premier nombre de la clé (p) :"))
	if estPremier(p):
		print("Le nombre choisis est premier")
		verif=True
	else:
		print("Le nombre choisis n'est pas premier recommencé")
		verif=False
verif=False
while verif != True :
	q=int(input("Entrez le premier nombre de la clé (q) :"))
	if estPremier(q):
		print("Le nombre choisis est premier")
		verif=True
	else:
		print("Le nombre choisis n'est pas premier recommencé")
		verif=False

n=p*q
phi=(p-1)*(q-1)
# On calcule e, un nombre aléatoire qui est premier avec phi(n)
verif=False
while verif!=True:
	e=randint(2,n)
	if sontPremiersEntreEux(e,phi):
		verif=True
	else:
		verif=False
print("La clé est "+str(n)+ " et "+str(e)) #affiche la clé pour validation visuelle
d=inv_modulo(e,phi)

#Génération de notre dictionnaire, il supporte tous les caractères ASCII depuis le 32 jusqu'au 215, nous avons fait ce choix pour pouvoir chiffrer des phrases
codageAlphabet=initialiseCodageAlphabet()
message=input("Entrez le message à chiffrer :")
expo=input("Voulez vous utiliser l'exponentiation modulaire ? (y/n)")

#Calcul en utilisant l'expo. modulaire
if expo == "n":
	debut = time.time()
	msgChiffre=chiffre(message)
	fin = time.time()
	tps = fin - debut
	
	print("Temps non optimisé :"+str(tps))
	print("Message chiffré :")
	afficheChiffre=''
	for i in msgChiffre:
		afficheChiffre+=str(i)
	print(afficheChiffre)
	print(msgChiffre)
	msgDechiffre=dechiffre(msgChiffre)
	print("Message déchiffré :")
	print(msgDechiffre)
#Calcul sans l'expo. modulaire
else:
	
	debut=time.time()
	msgChiffre=chiffreExpo(message)
	fin = time.time()
	tps = fin - debut
	
	print("Temps de chiffrement :"+str(tps))
	print("Message chiffre : ")
	afficheChiffre=''
	for i in msgChiffre:
		afficheChiffre+=str(i)
	print(afficheChiffre)
	print(msgChiffre)

	debut=time.time()
	msgDechiffre=dechiffreExpo(msgChiffre)
	fin = time.time()
	tps = fin - debut
	print("Temps de dechiffrement :"+str(tps))
	print("Message déchiffré :")
	print(msgDechiffre)
