


#1. Functia if else este o conditie care ia o anumita decizie daca sinaxa este adevarata. 
# In cazul in care sintaxa este falsa, intervine functia if else


# 2. 
#numarul natural = nr intreg pozitiv

x = 5
if x == int(x) and x > 0:
    print('x este numar natural')
else:
    print('x  nu este numar natural')

#3. 
x = 5
if x > 0:
    print("x este numar pozitiv")
elif x < 0:
    print("x este numar negativ")
elif x == 0:
    print("x este numar neutru")

#4.
x = 5
if x > -2 and x < 13:
    print("x se afla in intervalul -2 si 13")
else:
    print("x nu se afla in intervalul -2 si 13")


#5.
x = 5
y = 4
if (x - y) < 5:
    print("Diferenta dintre x si y este mai mica decat 5 ")
else:
    print("Diferenta dintre x si y nu este mai mica decat 5 ")



#6.
x = 4
if x != 5:
    print("Diferenta dintre x si y nu este mai mica decat 5 ")


#7.
x = 5
y = 4
if x == y:
    print("x este egal cu y")
elif x > y:
    print("x este mai mare decat y")
else:
    print("y este mai mare decat x")


#8.
x = 5
y = 4
z = 4
if x == y == z:
    print("triunghiul este echilateral")
elif y == z:
    print("triunghiul este isoscel")
else:
    print("triunghiul este oarecare")

#9. 
n = "e"
lst=["a", "e", "i", "o", "u"]
if n in lst:
    print ("e este vocala")
else:
     print ("e este consoana")

#10.
#Peste 9 => A
#Peste 8 => B
#Peste 7 => C
#Peste 6 => D
#Peste 4 => E
#4 sau sub => F

nota = input("Introduceti nota obtinuta")
nota = int(nota)
if nota > 9:
    print("Nota obtinuta este A ")
elif nota > 8:
    print("Nota obtinuta este B ")
elif nota > 7:
    print("Nota obtinuta este C ")
elif nota > 6:
    print("Nota obtinuta este D ")
elif nota > 4:
    print("Nota obtinuta este E ")
elif nota <= 4:
    print("Nota obtinuta este F ")



#11.
x = 246813
x = str(x)
if len(x) == 4:
    print("X are 4cifre")
else:
    print("X are mai mult de 4 cifre")





# In[73]:


#12.
x = 246813
x = str(x)
if len(x) == 6:
    print("X are exact 6 cifre")
else:
    print("X are mai mult de 6 cifre")


# In[76]:


#13.
x = 13
if x % 2 == 0:
    print("x este numar par")
else:
    print("x este numar impar")


# In[85]:


# 14.
x = 9
y = 15
z = 22
if x > y and x > z:
    print( "X este cel mai mare numar")
elif y > x and y > z:
    print( "Y este cel mai mare numar")
elif z > x and z > x:
    print( "Z este cel mai mare numar")


# In[86]:


#15


# In[115]:


#16.
my_string = "Coral is either the stupidest animal or the smartest rock"
x = 9
print(len((x)))


# In[ ]:





# In[119]:


# 23
x = input("Insert string here")

if len(x) % 2 == 0:
    print("Ati introdus un string de dimensiune para!!")
else:
     print("Ati introdus un string de dimensiune impara!!")

