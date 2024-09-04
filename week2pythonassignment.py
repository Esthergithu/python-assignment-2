#empty list
my_list = []
print(my_list)
#Append numbers
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After Append:",my_list)
#inserting the value 15 at the second position in the list
my_list.insert(1,15)
print(my_list)
#extend my list with another list
my_list.extend([50,60,70])
print(my_list)
#remove the last element from my list
del(my_list[7])
print(my_list)
#sort my list in ascending order
my_list.sort()
print(my_list)
#find and print the value of index 30 in my list
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)
