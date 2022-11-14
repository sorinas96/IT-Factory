#!/usr/bin/env python
# coding: utf-8

# In[11]:


#1. Clasa Cerc
#Atribute: raza, culoare
#Constructor pt ambele atribute

#Metode:
#descrie_cerc() - va PRINTA culoarea si raza
#aria() - va RETURNA aria 
#diametru() 
#circumferinta()
from math import pi
class Cerc:
    
    def __init__(self,raza,culoare):
        self.raza = raza
        self.culoare = culoare
    
    def descrie_cerc(self):
        print (f'Culoarea cercului este {self.culoare} si raza este {self.raza}')
    def aria(self):
        return pi*self.raza**2
    def diametru(self):    
        return  self.raza *2
    def circumferinta(self):
        return 2*pi*self.raza
c1 = Cerc(5,"rosu")
c2 = Cerc( 11, "albastru")

c1.descrie_cerc()
c2.descrie_cerc()
print(c1.aria())
print(c2.aria())
print(c1.diametru())
print(c2.diametru())
print(c1.circumferinta())
print(c2.circumferinta())


# In[24]:


#2. Clasa Dreptunghi

#Atribute: lungime, latime, culoare

#Constructor pt toate atributele

#Metode:
#descrie()
#aria()
#perimetrul()
#schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
#Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
#Puteti verifica schimbarea culorii prin apelarea metodei descrie().
class Dreptunghi:
    def __init__(self, lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
    def descrie_dreptunghi(self):
        print(f"Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}")
    def aria(self):
        return self.lungime * self.latime
    def perimetru(self):
        return 2 * self.latime + 2 * self.lungime
    def schimba_culoarea(self, culoare_noua):
        self.culoare = culoare_noua
d1 = Dreptunghi(20,10,"albastru")
d2 = Dreptunghi(44,33, "turcoaz")
d1.descrie_dreptunghi()
d2.descrie_dreptunghi()
print(d1.aria())
print(d2.aria())
print(d1.perimetru())
print(d2.perimetru())
d1.schimba_culoarea("galben")
d2.schimba_culoarea("purpuriu")
d1.descrie_dreptunghi()
d2.descrie_dreptunghi()


# In[39]:


#3.
#Clasa Angajat

#Atribute: nume, prenume, salariu

#Constructor pt toate atributele

#Metode:
#descrie()
#nume_complet()
#salariu_lunar()
#salariu_anual()
#marire_salariu(procent)

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self. salariu = salariu
    def descrie(self):
        print(f'Numele angajatului este {self.nume} {self.prenume} si are un salariu de {self. salariu} lei')
    def nume_complet(self):
        print(f'Numele complet al  angajatului este {self.nume} {self.prenume}')
    def salariu_lunar(self):
        print(f'Salariul lunar al angajatului este {self. salariu}')
    def salariu_anual(self):
        print(f'Salariul anual al angajatului este {self. salariu*12}')
    def marire_salariu(self)
        
a1 = Angajat("Popescu", "Ion", 3800)
a2 = Angajat("Abrudan", "Adrian", 8800)
a1.descrie()
a2.descrie()
a1.nume_complet()
a2.nume_complet()
a1.salariu_lunar()
a2.salariu_lunar()
a1.salariu_anual()
a2.salariu_anual()


# In[45]:


#4.Clasa Cont

#Atribute: iban, titular_cont, sold

#Constructor pentru toate

#Metode:
#afisare_sold() - Titularul x are in contul y suma de n lei
#debitare_cont(suma)
#creditare_cont(suma)

class Cont:
    def __init__(self, iban,titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
    def afisare_sold(self):
        print(f'Titularul { self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')
    def debitare_cont(self,suma):
        self.sold = self.sold + suma
        print(f'Titularul { self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')
    def creditare_cont(self, suma):
        if  self.sold > suma:
            self.sold -= suma
            return suma
        else:
            print("Fonduri insuficiente!")
            return 0
        
    
    
t1 = Cont("BTRLRONCRT123456789", "Popescu Ion", 1_000)
t2 = Cont("RORON123456789", "Popescu Flaviu", 1_000_000)

t1.afisare_sold()
t2.afisare_sold() 
t1.debitare_cont(3000)
t1.creditare_cont(2000)


# In[46]:


# 5.
from datetime import date
class Factura:
    serie = 'FDB'
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc
    def schimba_cantitatea(self, cantitatea_noua):
        self.cantitate = cantitatea_noua
    def schimba_pretul(self, pret_nou):
        self.pret_buc = pret_nou
    def schimba_nume_produs(self, nume_produs_nou):
        self.nume_produs = nume_produs_nou
    def genereaza_factura(self):
        print(f'Date: {date.today()}\nNume Produs|Cantitate|Pret|Total\n{self.nume_produs}|{self.cantitate}|{self.pret_buc}|{self.cantitate*self.pret_buc}')
    
f1 = Factura(5, 'Rimel', 3, 500)
f1.genereaza_factura()

f2 = Factura(9, 'Bocanci', 1, 700)
f2.genereaza_factura()


# In[47]:


# 7.
class TodoList:
    def __init__(self):
        self.todo = {}
        
    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
        
    def finalizeaza_task(self, nume):
        del self.todo[nume]
        
    def afiseaza_todo_list(self):
        print(list(self.todo.keys()))
        
    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task not in self.todo:
            to_add = input(f'Task {nume_task} nu exista in todolist. Il adaugam? [y/n]: ')
            if to_add.lower().startswith('y'):
                detalii = input(f'Descrierea taskului {nume_task}: ')
                self.todo[nume_task] = detalii
            else:
                print(f'Bun, la revedere!')
        else:
            print(f'>Task: {nume_task}\n>Descriere: {self.todo[nume_task]}')

todo_list = TodoList()
todo_list.afiseaza_todo_list()
todo_list.adauga_task('Cumparaturi Mall', '1. Haine, 2. Faina, 3. Oua, 4. Lapte')
todo_list.afiseaza_detalii_suplimentare('Repeta')


# In[ ]:




