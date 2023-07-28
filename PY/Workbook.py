"""digit = 72
sum = 0
sum = sum + int(digit)

print(sum)"""

"""a = 2 
a = 4 
a = 6 

print (a + a + a)"""

"""a=1 
b=2

print (a==b)
print (b==c)"""


# Python Program to input, append and print the list elements
# declare a list
"""myList = []
 
# take number from user, how many element in list
n = int (input ("How many element in list :- "))
 
 
# append element into list using list.append
for i in range (n) :
    storeElement = int (input ("Enter an integer num :- "))
    myList.append (storeElement)
 
# print all elements
print("Input list elements are: ")
for i in range (n) :
    print(myList [i])"""


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