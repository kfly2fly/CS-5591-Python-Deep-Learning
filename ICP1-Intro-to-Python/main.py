"""
1. State the differences between Python 2 and Python 3 version.

Ans: Python 3 is more used nowadays, many of today's developers are creating more libraries for python 3, Python 3 text strings aerr in unicode instead of ASCII by default, dividing gives you the expected result in python 3 instead of just the nearest whole number in python 2.
"""

#2.
#Initialize a string
myStr = "python"
#replace two characters with empty chars, deleting the characters
myStr = myStr.replace("h", '')
myStr = myStr.replace("o", '')
#Str[::-1] returns a reverse copy of the string
print(myStr[::-1])

#Asks user to input two numbers
x = int(input('Enter number 1: '))
y = int(input('Enter number 2: '))
#prints the arithmetic operations using string literals
print(f'{x} + {y} = {x+y}') 
print(f'{x} * {y} = {x*y}') 
print(f'{x} - {y} = {x-y}') 
print(f'{x} / {y} = {x/y}') 

#asks user for list of names (a string)
a = input("Input a list of names seperated by commas: ")
#We split the string into list
my_list = a.split(",")
#print the length of the list
print('The length of the list is:', len(my_list))
#Add a new name to the list
b = input('Add a new name to the list: ')
my_list.append(b)
print(my_list)

#3.

#Get a string from the user
myString = input("Enter a sentence. 'python' will be replaced by 'pythons': ")
#Replace all instances of 'python' with 'pythons'
myString = myString.replace('python', 'pythons')

print(myString)
  