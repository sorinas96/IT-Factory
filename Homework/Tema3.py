#!/usr/bin/env python
# coding: utf-8

# In[27]:


#1.a)
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do' ]
note_muzicale


# In[56]:


#b) Inverseaza ordinea folosind slicing si suprascrie aceasta lista
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale[:-9:-1])
note_muzicale = note_muzicale[:-9:-1]
print(note_muzicale)


# In[57]:


# c)Printeaza varianta actuala (inversata)
print(note_muzicale)


# In[59]:


#d)Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea.
note_muzicale.reverse()
print(note_muzicale)


# In[61]:


#e)Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
print(note_muzicale)


# In[63]:


#2.De cate ori apare ‘do’?

note_muzicale.count('do')


# In[104]:


#3. Varianta 1. CONCATENARE
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
print(list1+list2)
#Varianta 2
list1.extend(list2)
print(list1)


# In[106]:


#4.
list1.sort()
print(list1)
list1.remove(0)
print(list1)


# In[108]:


#5
list1 = [3, 1, 0, 2, 6, 5, 4]
if list1 == []:
    print('Lista este goala')
else:
    print('Lista nu este goala')


# In[109]:


#6.
list1.clear()
print(list1)


# In[110]:


#7
if list1 == []:
    print('Lista este goala')
else:
    print('Lista nu este goala')


# In[117]:


#8
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1.keys()
print("Elevii sunt:", list(dict1.keys()))


# In[123]:


#9.
print("Ana a luat nota: ", dict1.get("Ana"))
print("Gigel a luat nota: ", dict1.get("Gigel"))
print("Dorel a luat nota: ", dict1.get("Dorel"))


# In[146]:


#10
dict1.update({'Dorel' : 6})
print(dict1)


# In[159]:


#11
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1.pop('Gigel')
print(dict1)
dict1["Ionica"] = 9
print(dict1)


# In[165]:


#12.
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)
#nu da eroare, dar nici nu il adauga, deoarece seturile nu pot contine duplicate




# In[168]:


#13
if weekend & zile_sapt:
    print('Weekend este un subset al zilelor din sapt')
else:
     print('Weekend nu este un subset al zilelor din sapt')


# In[169]:


#14. 
print(weekend ^ zile_sapt)


# In[170]:


#15
print(weekend & zile_sapt)


# In[250]:


#16. Ne imaginam o echipa de fotbal pt teren sintetic.
#3 Schimbari maxime admise

#Declara o Lista cu 5 jucatori
#Schimbari_efectuate = va jucati voi cu valori diferite
#Schimbari_max = 3

#Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
#Efectuam schimbarea 
#Stergem jucatorul scos din lista
#Adaugam jucatorul intrat
#Afisam a intra x, a iesit y, mai aveti z schimbari

j = ['Ronaldo', 'Messi', 'Mbape', 'Neymar', 'Popescu']
Schimbari_max = 3
Schimbari_efectuate = 1
x = "Ronaldo"
y = "Pele"
if x in j and Schimbari_efectuate <= 3:
    print('Efectuam schimbarea')
else:
    print('Nu efectuam schimbarea')
    
j.remove('Ronaldo')
j  #jucatorul a fost sters
j.insert( 0 ,'Pele')
j # s-a adaugat jucatorul nou intrat
schimbari_ramase = 2
print("A intrat", y , 'a iesit', x , 'mai avem', schimbari_ramase , 'schimbari'  )

#Daca jucatorul nu e in teren:
#Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
#Afisati ‘mai aveti z schimbari
schimbari_ramase = 3
if x not in j :
    print('Nu se poate efectua schimbarea deoarece jucatorul', x, 'nu e in teren.'' Mai aveti', schimbari_ramase, 'schimbari ramase' )


# In[ ]:




