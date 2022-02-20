#import requests

#link = 'http://danielrusak.pl/kubus_puchatek'
#kubus_raw = requests.get(link)
#print(kubus_raw)


import requests

link = 'http://danielrusak.pl/kubus_puchatek'
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text
print(kubus_text)


kubus_text = []
n = int(input(kubus_text))
for i in range(n):
	new_element = int(input(kubus_text)) # przeczytaj następny element
a.append(new_element)
print(a)
