
#importy / biblioteki
#import requests  #gdzies jest w necie do pobrania za pomoca pip3, dokumentacja jej, wersja. Biblioteka 
#link = 'http://zajecia-programowania-xd.pl/flagi'
#flagi = requests.get(link)
#flagi = flagi.text
#print(flagi)	

#listy
#lista = [1, 2, 3]
#lista = 'aagshshjdjdk'
#dlugosc_listy = len(lista)
#print('Dlugosc:', dlugosc_listy)
#element = lista[2]
#print('Element:', element)


#petle

#for element in lista
#	print (element)


import requests
link = 'http://zajecia-programowania-xd.pl/flagi'
flagi_response = requests.get(link)
flagi_tekst = str(flagi_response.text.encode('utf-8'))
#flagi_tekst = flagi_response.text.encode('utf-8')
print(flagi_tekst)

flagi = flagi_tekst.split('</p>')
#flagi = flagi_tekst.split(b'</p>')
#for f in flagi:
#	print(f)
#for f in flagi:
#	if (b'http://') in f:
#		f = f[3:]
#		print('-', f)
for f in flagi:	
	if 'http://' in f:
		f = f[3:] # bez 3 pierwszych znakow <p> 
		print('-', f) #flagi beda poprzedzone z myslnikami

