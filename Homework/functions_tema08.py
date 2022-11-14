#1. Creati-va 2 fisiere separate, unul numit functions_tema08.py, in care sa adaugati implementarea
# , iar altul numit test_functions_tema08.py in care sa aveti clasa de test.
#a) Scrieti o functie care primeste un numar natural si returneaza daca e prim sau nu

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


print(is_prime(3))

#2.Scrieti o functie care are 2 parametrii nr naturale a,b cu a<b.
# Functia returneaza lista numerelor prime din intervalul [a,b].

def prime_numbers (a,b)
  print("Prime numbers between", lower, "and", upper, "are:")
  for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
      for i in range(2, num):
        if (num % i) == 0:
          break
      else:
        print(num)