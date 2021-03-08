#! python3
"""
Print the list named "fruit".
Ask the user to enter a word
If the word is in the list, delete all occurrences of that word from the list
If the word is not in the list, add the word to the list
Print out the updated list

inputs:
string

outputs:
list

examples:
['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi']
Enter a word from the list:kiwi
['apple', 'cherry', 'apple', 'banana', 'strawberry', 'blueberry']

['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi']
Enter a word from the list:orange
word not in list
['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi', 'orange']

"""

fruit = ["apple","cherry","kiwi","apple","banana","strawberry","kiwi","blueberry","kiwi"]

name = input("Enter a word from the list:")

if name == "apple":
    fruit.remove("apple")
    fruit.remove("apple")
    print(fruit)
elif name == "cherry":
    fruit.remove("cherry")
    print(fruit)
elif name == "kiwi":
    fruit.remove("kiwi")
    fruit.remove("kiwi")
    fruit.remove("kiwi")
    print(fruit)
elif name == "banana":
    fruit.remove("banana")
    print(fruit)
elif name == "strawberry":
    fruit.remove("strawberry")
    print(fruit)
elif name == "blueberry":
    fruit.remove("blueberry")
    print(fruit)
else:
    fruit.insert(9, name)
    print(fruit)



