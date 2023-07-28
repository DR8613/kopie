WordsList = []
n = int(input ("How many elements in words list: "))
for w in range(n):
    strings=str(input ("Enter string: "))
    WordsList.append(strings)

#print(set(WordsList)) # change to set to avoid duplicates
print(dict(WordsList))