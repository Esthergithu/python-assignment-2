#question one(on lists)
my_list = [1,3,5,7,9]
print(sum(my_list))
#question two(on tuples)
Books = ("When Tomorrow Comes", "Feel the Fear and Do it Anyway", "Yellow Face", "A Leader With No Title", "Becoming")
for Book in Books:
    print(Book)
#question three(on dictionaries)
Personal_info = {}
#ask for the user's input
Personal_info['Name'] = input("Enter your name:")
Personal_info['Age'] = input("Enter your age")
Personal_info['Favourite Colour'] = input("Enter your favourite colour:")
#print the dictionary to the console
print(Personal_info)
#question four(on sets)
def get_integer_set(prompt):
    user_input = input(prompt)
#get user input for two sets
set1 = get_integer_set("Enter integers for the first set,separates by spaces: ")
set2 = get_integer_set("Enter integers for the second set, separated by spaces: ")
#find the common elements between two sets
common_set = set1.intersection(set2)
#output the result
print("The common elements between the two sets are: ",common_set)

#question five(on lists)
words = ['Kenya','Uganda','Mali','Gambia','Morocco','Gabon','Malawi']
odd_length_words = [word for word in words if len(word)% 2 !=0]
#print the original list and the new list
print("Original list of Words:", words)
print("words with an odd number of characters:", odd_length_words)