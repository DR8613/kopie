import random
import string

#Generator hasla
#ciag znakow
#string
#losowe haslo

#haslo = ''
#for i in range(10):
#    haslo += random.sample(lowercase, 1)[0]
#print(list)range
# duze litery , 2
# male litery, 2
# znaki specjalne, 2
# liczby , 2

n_znakow = 8  #def.liczby znakow ile znakow chce
n_znakow_typu = 2

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation
digits = string.digits

wszystkie_znaki = lowercase + uppercase + punctuation + digits
#losowy_znaki = random.sample(lowercase, 8)
losowe_znaki = random.sample(wszystkie_znaki, n_znakow)

haslo = ''.join(losowe_znaki)

print(digits)
print(punctuation)
print(lowercase)
print(uppercase)
print(haslo)
#print(haslo, type(haslo))
#print(haslo[0], type(haslo[0]))
print()
