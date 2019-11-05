from random import randrange
import math
from math import gcd
import time

'''
source:
RSA:
http://www.crittologia.eu/critto/rsa/metodo.html
https://gist.github.com/JonCooperWorks/5314103
https://hackernoon.com/how-does-rsa-work-f44918df914b
http://math.infopervoi.altervista.org/matematica/scomposizione_in_fattori_primi.php?ln=it
libreria grafica:
https://docs.python.org/3/library/tkinter.html
https://effbot.org/tkinterbook/button.htm
'''

class Chiave:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        
        self.n = p*q
        self.b = (p-1)*(q-1)

        #cerca "e" a random fino a quando non ne trova uno coprimo
        self.e = int(randrange(self.b))
        while (not(coprime(self.e, self.b))):
            self.e = int(randrange(self.b))

        #trova "d" grazie all'applicazione del teorema esteso di Euclide
        self.d = multiplicative_inverse(self.e,self.b)

#qui la roba copiata

def multiplicative_inverse(e, b):#in uso
    x = 0
    y = 1
    lx = 1
    ly = 0
    oe = e  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = e // b
        (e, b) = (b, e % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    if ly < 0:
        ly += oe  # If neg wrap modulo orignal a
    # return a , lx, ly  # Return only positive values
    return lx



#qui la roba fatta

def coprime(e, b):
    return gcd(e, b) == 1

def crypt(s, chiave):
    s = list(s)
    intList = char_list_to_int(s)

    i = 0
    crypted = intList
    tick = time.time()
    while i < len(crypted):
        crypted[i] = pow(intList[i], chiave.e, chiave.n)
        i = i + 1
    print(" --tempo per la crittazione: " + str(time.time() - tick) + "--")
    return crypted
	
def decrypt(crypted, chiave):
	tick=time.time()
	decrypted = crypted
	i = 0
	while i < len(decrypted):
		decrypted[i] = pow(crypted[i], aldo.d, aldo.n)
		i = i + 1
	print(" --tempo per la decrittazione: " + str(time.time()-tick) + "--")
	return decrypted

def char_list_to_int(listChar):#fa quello che dice
    i = 0
    listInt = listChar
    while i < len(listChar):
        listInt[i] = ord(listChar[i])
        i = i + 1
    return listInt

def int_list_to_char(listInt):#fa quello che dice
    i = 0
    listChar = listInt
    while i < len(listInt):
        listChar[i] = chr(listInt[i])
        i = i + 1
    return listChar

def char_list_to_string(s):#fa quello che dice
    new = "" 
    for x in s: 
        new += x
    return new 
	
	
#----------------------------------------------------main------------------------------------------------
#messaggio
s = input("Inserisci il messaggio\n")


#generazione chiavi
#n,e,d
tick=time.time()
aldo = Chiave(101595101, 999999937)
print()
print("n: " + str(aldo.n) + " e: " + str(aldo.e) + " d: " + str(aldo.d))
print()
print(" --tempo per la generazione: " + str(time.time()-tick) + "--")

#crittazione
#c = s^e mod n
crypted = crypt(s, aldo)
print("messaggio criptato: " + str(crypted))

#decrittazione
#s = c^d mod n
decrypted = decrypt(crypted, aldo)
   

print("messaggio decriptato: " + str(decrypted))
print("messaggio decriptato e convertito: ")
decrypted = int_list_to_char(decrypted)
print(char_list_to_string(decrypted))

