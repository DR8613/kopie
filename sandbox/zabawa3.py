			

#x = 10
#print (x, type (x))

#y = '10'
#print (y, type(y))

#z = 10.2
#print (z ,type(z)) 

#moja_zmienna = 0
#dzien = 'sroda'

#if dzien == 'poniedzialek':
#	print (1) #('dzisiaj jest sroda')
#else:
#	print (0) #('nie dzis nie jest sroda')


#email_usera = 'admin@wp.pl'
#email_w_bazie = 'tes2t@wp.pl'
#if email_usera == email_w_bazie :
#	print ('Email zgadza sie')
#elif  email_usera == 'admin@wp.pl':
#	print ('Uzyles maila admina')
#else:
#	print ('Email nie poprawny')

dzien = 'Poniedzialek'
dzisiaj = 'Wtorek'

dni_pracujace = [
	'Poniedzialek',
	'Wtorek',
	'Sroda',
	'Czwartek',
	'Piatek',
]

weekend = [	
	'Sobota',
	'Niedziela',
]

if dzisiaj == dzien :
	print ('Dzisiaj jest', dzisiaj)
elif dzien in dni_pracujace:
	print ('Dzisiaj jest dzien pracujacy', dzisiaj)
elif dzien in weekend:
	print ('Dzisiaj jest weekend') 
else:
	print ('Zle napisales dzien tygodnia')

