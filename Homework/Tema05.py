#!/usr/bin/env python
# coding: utf-8

# In[7]:


#1. Functie care sa calculeze si sa returneze suma a 2 numere
#v1
def sum_2nr(a,b):
    return(a + b)

s = sum_2nr(10,15)
print(s)

#v2

def sum_2nr(a,b):
    return(a + b)

s = sum_2nr(14,14)
print(s)


# In[13]:


#2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def find(num):
    if num % 2 == 0:
        numtype = "even"
        print(True)
    else:
        numtype = "odd"
        print(False)
    return numtype
num = int(input(f'Enter number here: '))
numtype = find(num)


# In[20]:


#3. Functie care returneaza numarul total de caractere din numele tau complet.
#(nume, prenume, nume_mijlociu)
def count_chars(text):
    result = 0
    for char in text:
        result +=1
    return result
print(count_chars('Sorina-Sateanu-Maria'))



# In[33]:


#4. Functie care returneaza aria dreptunghiului

def rectangle_area(width, height):
    area =  width*height
    return area
areaA = rectangle_area(4,6)
print(f'Aria dreptunghiului este: {areaA}')
areaB = rectangle_area(20,30)
print(f'Aria dreptunghiului este: {areaA}')


# In[36]:


#5. Functie care returneaza aria cercului
def circle_area(pi,R):
    area = pi*R**2
    pi = 3.14
    return area
areaA = circle_area(3.14, 2)
print(f'Aria cercului este: {areaA}')
areaB = circle_area(3.14, 4)
print(f'Aria cercului este: {areaB}')


# In[57]:


#6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu


def find_char(x):
    my_string = "It is monday again"
    if "x" in my_string:
        return True
        print(True )
    else:
        return False
        print(False )


# In[164]:


#7. Functie fara return, primeste un string si printeaza pe ecran:
#Nr de caractere lower case este x
#Nr de caractere upper case exte y 
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("String Original : ", s)
    print ("Caractere Uppercase : ", d["UPPER_CASE"])
    print ("Caractere Lowercase : ", d["LOWER_CASE"])

string_test(f'It is monday again')
    


# In[68]:


#8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive


numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
def negative_list(numere):
    for idx in range(len(numere)):
        if numere[idx] > 0:
            numere[idx] = -numere[idx]
print(negative_list)


# In[71]:


#9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
#Primul numar x este mai mare decat al doilea nr y
#Al doilea nr y este mai mare decat primul nr x
#Numerele sunt egale. 
def numere(x,y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    if x < y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}.')
    if x == y:
         print(f'Numerele sunt egale')
numere(5,6)
numere(9,4)
numere(4,4)


# In[93]:


#10. Functie care primeste un numar si un set de numere.
#Printeaza ‘am adaugat numarul nou in set’ + returneaza True
#Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
def my_set(x,y):
    s = my_set([2,3,4,5])
    s.add(x) 
print (f'Am adaugat numarul nou in set')
print(True)
s.add(y) 
print (f'nu am adaugat numarul in set. Acesta exista deja')
print(False)
my_set(3,99)


# In[97]:


#11. Functie care primeste o luna din an si returneaza cate zile are acea luna
from calendar import monthrange
def number_of_days_in_month(year=2022, month=10):
    return monthrange(year, month)[1]
print(number_of_days_in_month(2022, 10))


# In[107]:


#12.Functie calculator care sa returneze 4 valori 
#Suma, diferenta, inmultirea, impartirea a 2 numere


def adunare(x, y):
    return x + y


def scadere(x, y):
    return x - y


def inmultire(x, y):
    return x * y


def impartire(x, y):
    return x / y


print("Selectati operatiunea dorita.")
print("1.Adunare")
print("2.Scadere")
print("3.Inmultire")
print("4.Impartire")

while True:
    
    choice = input("Selectati operatiunea dorita(1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Alegeti primul numar: "))
        num2 = float(input("Alegeti al doilea numar: "))

        if choice == '1':
            print(num1, "+", num2, "=", adunare(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", scadere(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", inmultire(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", impartire(num1, num2))
        
        
        operatia_urmatoare = input("Mai facem o operatie? (da/nu): ")
        if operatia_urmatoare == "nu":
          break
    
    else:
        print("Invalid Input")


# In[110]:


#14
#v1
def maxim(a, b, c):
    lst = [a, b, c]
    return max(lst)


print(maxim(10, 2, 4))

#v2
def maxim(a, b, c):
    lst = [a, b, c]
    return max(lst)

a = 10  
b = 14
c = 12
print(maxim(a, b, c))


# In[139]:


#17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
#Returnati numerele comune
def element_comun(a, b):
    result = [i for i in a if i in b]
    return result
 
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

print(f'elementele comune sunt : {element_comun(a, b)}')


# In[163]:


#21.

def gen(text):
       return (gen)
def last_letter(x):
        if last_letter == "a":
            print(f'Numele este de fata')
        else:
            print(f'Numele este de baiat')
    
gen('Alexa')


# In[ ]:




