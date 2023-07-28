"""#Count Vowels Write a function that takes a string as input and returns 
the count of vowels (a, e, i, o, u) in the string."""

s = str(input("Enter string: "))
print(s)

"""def count_vowels(s):
    # Initialize variables to keep track of counts for each vowel.
    num_a = 0
    num_e = 0
    num_i = 0
    num_o = 0
    num_u = 0
    # Loop through all characters in the given string.
    for char in s:
        if char == 'a' or char == 'A':
            num_a +=1
        elif char == 'e' or char == 'E':
            num_e +=1 
        elif char == 'i' or char == 'I':
            num_i +=1
        elif char == 'o' or char =='O':
            num_o +=1
        elif char=='u'or char=='U':
            num_u +=1
        print (count_vowels(char))
    return (count_vowels(s)) 
result=count_vowels('s')
print(result)"""

def countVovels(s):
    vowels= {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    #vowels2= 
    for char in s:
        if char.lower() in vowels:
            vowels[char] += 1

    return vowels


"""elif: char.upper() in vowels2:
            for char in s:
                if char.upper() in vowels2:
                vowels2[char] += 1
            return vowels2"""
    
print(countVovels(s))
    




        

