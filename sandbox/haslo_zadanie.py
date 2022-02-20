import random
import string

n_znakow = 8  #def.liczby znakow ile znakow chce
#n_znakow_typu = 2  - nie wiem po co to xD

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation
digits = string.digits

#wszystkie_znaki = lowercase + uppercase + punctuation + digits
#losowe_znaki = random.sample(wszystkie_znaki, n_znakow)

uppercasee_2 = random.sample(uppercase, 2) #losowe 2 duze litery
lowercase_2 = random.sample(lowercase, 2) #losowe 2 male litery
punctuation_2 = random.sample(punctuation, 2) #losowe 2 znaki specjalne
digits_2 = random.sample(digits, 2) #losowe 2 liczby

wszystkie_znaki = uppercasee_2 + lowercase_2 + punctuation_2 + digits_2  #zlaczenie powyzszych dwóch liczb,cyfr,liter(male/duze) w jeden ciag znakow
password = random.sample(wszystkie_znaki, n_znakow) # wymiesznie laczonego ciagu znakow

haslo = ''.join(password) # przypisanie wygenerowanego hasla do pustej zmienniej 'haslo'

print('Hasło:' + ' ' + haslo) # wydruk hasla na ekranie
print()