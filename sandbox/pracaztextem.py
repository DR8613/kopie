import requests



#def nazwa_funkcji(argument1):

def policz_znaki(string):
	dlugosc_stringu = len(string)
	return dlugosc_stringu




#def policz_znaki(argument):
#	liczna_znakow = len(argument)
#	return liczba_znakow 


link = 'https://zajecia-programowania-xd.pl/kubus_puchatek' 
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text #.encode('utf-8'))



#x = 'abc' #str
#y = 1 # int
#z = 0.0001 # float

#funkcje 


#x = 'string'
#y = len(x)

#print(x)
#print(y)

#indekst
#link_b = link[0]
#link_b = link[10]
#link_b = link[::-1]

#metody wbudowane
#link_b = link.upper() #lower

#dodawanie ciagow znakow
#link_b = link[:21].upper()  + '    ' + link[10:] 

#Dzielenie ciagow znakow
#split()

#ciag = 'abcd abcd abcd abcd'
ciag = 'tutaj sa jakies slowa'
efekt = ciag.split('a')


print()
print(link)
print(ciag)
print(efekt)
print()
