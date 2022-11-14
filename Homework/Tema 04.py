#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.Folositi un for ca sa iterati prin toata lista cu ajutorul indexilor si sa afisati ‘Masina mea preferata este x’
#a)

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel'] 
for idx in range(len(masini)):
    print(idx, masini[idx])
print(f'Masina mea preferata este {masini[4]}')


# In[16]:


# b.Faceti acelasi lucru cu un for each

for item in enumerate(masini):
    print(item)
print(f'Masina mea preferata este {masini[4]}')


# In[ ]:


# c. Faceti acelasi lucru cu un while


# In[40]:


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
i = 0
lenght = len(masini)
while i < lenght:
    print (masini[i])
    i+=1
print(f'Masina mea preferata este: {masini[4]} ')


# In[67]:


#2.Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
#(v1 - caracter, v2 - element)
 #v1.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for x in masini:
    #print(x.upper())
    for y in masini:
        y = masini[0:1]
    #print (y)
    x = str(x.replace(y, x.upper()))


# In[171]:


#.3#Vine un cumparator care doreste sa cumpere un Mercedes
#Iterati prin ea cu for
#Daca masina e mercedes (if)
  # Printam ‘am gasit masina dorita de dvs’
   #Iesim din ciclu folosind un cuvant cheie care face acest lucru
#Altfel:   
 #  Printam Am gasit masina X. Mai cautam
    
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for elem in masini[3]:
    print(elem)
for x in masini:
    if x == "Mercedes":
        print(f'Am gasit masina dorita de dvs')
        break 
    else:
        print(f'Am gasit masina {x}. Mai cautam')


# In[178]:


# 4.
# Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun. 
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for elem in masini:
    if elem =="Lastun":
        continue
    if elem  =="Trabant":
        continue
    print(f'S-ar putea sa va placa masina {elem}')


# In[206]:


# 5. Modernizati parcul de masini
#Creati o lista goala, masini_vechi
#Iterati prin masini
#Cand gasiti Lastun sau Trabant:
#Salvati aceste masini in masini_vechi
#Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
#Printati Modele vechi: x
#Modele noi: x
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for x in masini:
    if x =="Lastun":
        masini_vechi.append(x)
        masini.remove(x)
        masini.append("Tesla")
    if x =="Trabant":
        masini_vechi.append(x)
        masini.remove(x)
        masini.append("Tesla")
        print(masini_vechi)
        print(masini)


# In[224]:


#6. Avand dict
#pret_masini = {
#    'Dacia': 6800,
#    'Lastun': 500,
#    'Opel': 1100,
#    'Audi': 19000,
#    'BMW': 23000
#}
#Vine un client cu un buget de 15000 euro
#Prezentati doar masinile care se incadreaza in acest buget
#Iterati prin dict.items() si accesati masina si pretul
#Printati Pentru un buget de sub 15000 euro puteti alege masina x
#Iterati prin lista

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget_client = 1500

for x,y in pret_masini.items():
    if y <= buget_client:
        print(f' Pentru un buget sub {buget_client} puteti alege masina {x} avand pretul de {y}')


# In[240]:


# 7.
# Avand lista
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
y = 0

for x in numere:
    if x == 3:
        y+=1
print(f'Numarul {x} apare de {y} ori')


# In[245]:


# 8
# Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lenght = len(numere)-1
for x in range(lenght):
    if numere[x]> numere[x+1]:
        numere[x], numere[x+1] = numere[x+1], numere[x]
print(numere[-1])



# In[ ]:


# 9.


# In[330]:


# 10.
# Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for x in range(len(numere)):
        numere[x]= - numere[x] 
print(f'Lista in urma modificarilor este: {numere}')


# In[288]:


# 11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
# Iterati prin lista alte_numere 
# Populati corect celelalte liste
# Afisati cele 4 liste la final
for i in alte_numere:
    if i % 2 == 0 and i > 0 :
        numere_pare.append(i)
    if i % 2 != 0 and  i > 0:
        numere_impare.append(i)
    if  i > 0:
        numere_pozitive.append(i)
    if  i < 0:   
        numere_negative.append(i)        
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print( numere_negative)


# In[296]:


# 12.
# Aceeasi lista
# Ordonati crescator lista fara sa folositi sort
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere = []
    
while alte_numere:
    min = alte_numere[0]
    for x in alte_numere:
         if x < min:
            min = x
    numere.append(min)
    alte_numere.remove(min)
print(numere)


# In[298]:


# 13.
# Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!
import random
random.randint(1,30)


# In[324]:


#14. 
rows = int(input("Enter number of rows: "))

for a in range(rows):
    for b in range (a+1):
        print('1', end = "")
    print ("\n")
    for c in range (a+2):
        print('2', end = "")
    print ("\n")
    for d in range (a+3):
        print('3', end = "")
    print ("\n")
    for e in range (a+4):
        print('4', end = "")
    print ("\n")


# In[328]:


# 15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
# Iterati prin lista 2d
# Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)
#x = [ ['0,0', '0,1'], ['1,0', '1,1'], ['2,0', '2,1'] ]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este: {tastatura_telefon[i][j]}')


# In[ ]:




