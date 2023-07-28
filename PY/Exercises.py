"""
#Ex.1 Print all even numbers from range
startRange = int(input ("Enter start of the range:"))
endRange = int(input ("Enter end of the range: "))

for num in range(startRange, endRange+1):
    if num % 2 == 0:
        print (num)
"""


#Ex.2 Sum of digits 



"""number= str(input("Enter the number: "))
sum=0
for digit in number:
    sum = sum + int(digit)
print("Sum of the digits", sum)"""


"""number= input("Enter the number: ")
sum=0
for digit in str(number):
    sum = sum + int(digit)
print("Sum of the digits", sum)"""

"""number= int(input("Enter number: "))
sum_of_digits=0
for digit in str(number):
    sum_of_digits = sum_of_digits + int(digit)
print ("Sum of digits",(number),":", sum_of_digits)"""

#sum_of_digits = sum([int(i) for i in str(abs(digit


#Ex.3
 
#Works

"""
s=''
for i in range(7):
    s+='*'
    print (s)
"""

"""
size = int(input("Enter amount of rows: "))

for row in range(size):
    for  tri in range(row+1):
        print("*",end= " ")
    print()
"""

"""
row = int (input("Enter amount of rows: "))
size = row

for row in range(size):
    for tri in range(row + 1):
        print('*', end='')
    print() 
"""

#DataStructures

"""mylist=[]
sum = 0
mylist = (input("Enter list of digits:"))
for d in str(mylist):                           #nie działa
    sum = sum + int(mylist)
print(sum)"""

#"Sum of all numbers in the list:"
mylist =[]
sum = 0
n = int(input ("How many elements in list: "))
#using list.append
for i in range(n):
    values=int(input ("Enter integer num: "))
    mylist.append(values)
    print(values)
#print all numbers 
#for i in range(n):
    
#sum of digit from list
for j in range(n):
    sum = sum + mylist[j]
print("Sum of all numbers in the list:", (sum))

# Program that takes a list of words as input and remove duplicates
"""WordsList = []
n = int(input ("How many elements in words list: "))
for w in range(n):
    strings=str(input ("Enter string: "))
    WordsList.append(strings)

print(set(WordsList)) # change to set to avoid duplicates
#print(dict(WordsList))# change to dictionary to avoid duplicates

#Create a program that takes a list of students and thair corresponding scores as input and converts it into dictionary
#Stundets = []
#Scores = []
#st = int(input ("How many elements in students list: "))
#sc = int(input ("How many scores for each element?"))
"""while st==sc:
        for i in range(st):
                strings = str(input ("Enter student name: "))
                Stundets.append(strings)
        print(Stundets)
        for j in range(sc):
                strings = str(input ("Enter student score: "))
                Scores.append(strings)
        print(Scores)
        print("Students and thair corresponding scores:" , dict(zip(Stundets,Scores)))
        break
else:
    print("Error! Number of Student Names should be equal to number of their respective Score")
    

if st==sc:
    for i in range(st):
            strings = str(input ("Enter student name: "))
            Stundets.append(strings)
    print(Stundets)#for checking
    for j in range(sc):
            strings = str(input ("Enter student score: "))
            Scores.append(strings)
    print(Scores)#for checking
    print("Students and thair corresponding scores:\n" , dict(zip(Stundets,Scores)))
        
else:
    print("Error! Number of Student Names should be equal to number of their respective Score")"""
  
   
