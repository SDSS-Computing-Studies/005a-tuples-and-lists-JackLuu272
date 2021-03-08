#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""

list = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(list)
choice = input("Choose a person from the list to replace:")
replace = input("Enter the replacement:")
 
if choice == "Alain":
    list.pop(0)
    list.insert(0, replace)
    print(list)
elif choice == "Brian":
    list.pop(1)
    list.insert(1, replace)
    print(list)
elif choice == "Chris":
    list.pop(2)
    list.insert(2, replace)
    print(list)
elif choice == "Justin":
    list.pop(3)
    list.insert(3, replace)
    print(list)
elif choice == "Angela":
    list.pop(4)
    list.insert(4, replace)
    print(list)
else:
    list.pop(5)
    list.insert(5, replace)
    print (list)

