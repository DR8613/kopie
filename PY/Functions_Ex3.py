#Calculate Factorial.Write a function to calculate the factorial of a given number using recursion.​

import math 

n = int(input("Enter the number: "))

def fact(n):
    if n ==0:
        return 1
    else :
        return (fact(n-1)*n)
print ("The Factorial is ",fact(n))
#print("Factorial of",(n),"is:",math.factorial(n))
    #using inbuilt library for calculating factorial