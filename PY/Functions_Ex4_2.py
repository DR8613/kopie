s = str(input("Enter string: "))
print(s)

def countVovels(s):
    vowels= {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'A':0, 'E':0, 'I':0, 'O':0, 'U':0 }

    for char in s:
        if char in vowels:
            vowels[char] += 1
    return vowels
  
print(countVovels(s))

""" 
"KISS"
Keep It Simple, Stupid..
"""