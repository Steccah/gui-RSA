import tkinter as tk
from random import randrange
import math
from math import gcd


class Application(tk.Frame):
    generated = False
    inputted = False

    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #top text
        self.title = tk.Label(self, bg = "#F0F0F0", font = "Segoe 10", text = "RSA")
        self.title.pack()

        #entry
        self.entry = tk.Entry(self)
        self.entry.pack(fill=tk.X)
        

        #confirm entry
        self.get = tk.Button(self, bg = "white", relief = "groove", text="conferma", command = self.get_input)
        self.get.pack()

        #generate
        self.gen = tk.Button(self, bg = "white", relief = "groove", text="Genera",
                             command = self.generate)
        self.gen.pack(ipadx = 10, ipady = 10, pady = 5)

        #crypt
        self.cry = tk.Button(self, bg = "white", relief = "groove", text="Cripta", state = "disabled",
                             command = self.crypt)
        self.cry.pack(ipadx = 10, pady = 5)

        #decrypt
        self.decry = tk.Button(self, bg = "white", relief = "groove", text="Decripta", state = "disabled",
                               command = self.decrypt)
        self.decry.pack(ipadx = 10, pady = 5)

        #quit
        self.quit = tk.Button(self, bg = "white", relief = "groove", text="quit", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side = "bottom", padx = 5, fill=tk.X)

        #BOTTOM TEXT
        self.output = tk.Text(self, bg = "white", font = "Segoe 10", relief = "flat")
        self.output.pack(fill = tk.X)

        

    def generate(self):
        self.chiave1 = Chiave(101595101, 999999937)
        self.generated = True
        print("generated")
        if(self.inputted):
            self.cry.config(state = "normal")

    def crypt(self):
        global m
        m = crypt(m, self.chiave1)
        print(m)
        self.gen.config(relief="sunken", bg = "#ff6060", state = "disabled")
        self.decry["state"] = "normal"
        self.output.insert(tk.END, str(m) + "\n")

    def decrypt(self):
        global m
        m = decrypt(m, self.chiave1)
        print(m)
        self.output.insert(tk.END, str(m) + "\n")

    def get_input(self):
        global m
        m = self.entry.get()
        m = list(m)
        m = char_list_to_int(m)
        print(m)
        self.inputted = True
        if(len(m)>0 and self.generated):
            self.cry.config(state = "normal")
        elif(self.generated):
            print("messaggio non abbastanza lungo")
            self.cry["state"] = self.decry["state"] = "disabled"
        else:
            print("prima devi generare le chiavi")
            self.cry["state"] = self.decry["state"] = "disabled"

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


#---------------------------------------------------------------------#
'''metodi'''

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
    i = 0
    crypted = s
    while i < len(crypted):
        crypted[i] = pow(s[i], chiave.e, chiave.n)
        i = i + 1
    return crypted
	
def decrypt(crypted, chiave):
    i = 0
    decrypted = crypted
    while i < len(decrypted):
        decrypted[i] = pow(crypted[i], chiave.d, chiave.n)
        i = i + 1
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
#----------------------------------------------------------------------------------#
'''main'''

root = tk.Tk()
app = Application(master=root)
app.mainloop()

