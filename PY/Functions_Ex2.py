mylist = []
n = int(input("How many values?:"))

for i in range(n):
    values =int(input ("Enter integer num: "))
    mylist.append(values)
print(mylist)

def maxOflist(mylist):
    max = 0
    for num in mylist:
        if num > max:
            max=num
    return max
result = maxOflist(mylist)
print(result)

"""def maxvalue (values):

    
    for i in range(n):
        
        
        if i > max:
            return max
        
    print(values)
#return mylist[0] if len([x for x in mylist]) == 1"""
    