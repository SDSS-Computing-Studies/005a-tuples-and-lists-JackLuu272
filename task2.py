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

x = input("Enter a word: ").strip()
y = input("Enter a word: ").strip()
z = input("Enter a word: ").strip()
a = input("Enter a word: ").strrip()
b = input("Enter a word: ").strip()
List = [x,y,z,a,b]
print("\n" + str(List))