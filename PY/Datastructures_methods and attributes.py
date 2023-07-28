my_list = [1,2,3,4] 

#creating 'doubled' list
my_doubled_list =[]
for number in my_list:
    my_doubled_list.append(2*number)
"""print(my_list)
print("\n")
print(my_doubled_list)"""
print(my_list)
print( [2*number for number in my_list] )