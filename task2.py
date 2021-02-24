#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""

x = input("Enter a word: ")
y = input("Enter a word: ")
z = input("Enter a word: ")
a = input("Enter a word: ")
b = input("Enter a word: ")

List = [x,y,z,a,b]
print("\n")
print(str(List))