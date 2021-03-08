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
    list.remove('Alain')
    list.insert(0, replace)
    print(list)
elif choice == "Brian":
    list.remove("Brian")
    list.insert(1, replace)
    print(list)
elif choice == "Chris":
    list.remove("Chris")
    list.insert(2, replace)
    print(list)
elif choice == "Justin":
    list.remove("Justin")
    list.insert(3, replace)
    print(list)
elif choice == "Angela":
    list.remove("Angela")
    list.insert(4, replace)
    print(list)
else:
    list.remove("Rick")
    list.insert(5, replace)
    print (list)

