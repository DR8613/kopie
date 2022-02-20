import requests

link = 'https://zajecia-programowania-xd.pl/kubus_puchatek'
kubus_raw = requests.get(link)
kubus_text = kubus_raw.text #.encode('utf-8'))
#kubus_text = kubus_text.replace('<p>',  'xd' )
kubus_text = kubus_text.replace('<p>' , ' ')
kubus_text = kubus_text.replace('</p>' , ' ')

dlugosc_kubusia = len(kubus_text)
print(kubus_text)
print(dlugosc_kubusia)

kubus_puchatek_slowa = kubus_text.split()
kubus_puchatek_slowa_n = len(kubus_puchatek_slowa)
print(type(kubus_puchatek_slowa_n))
print(kubus_puchatek_slowa_n)

kubus_n = 0
#for i, s in enumerate(kubus_puchatek_slowa):
for s in [kubus_puchatek_slowa]:
	if s == 'Kubu':
		print(s)
	kubus_n = kubus_n + 2

	#kubus_n +=1
	#s = 'Kubuś'
#	if 'Kubuś' in s:	
#		print(i, s)
#		kubus_n +=1
print(kubus_n)
	
