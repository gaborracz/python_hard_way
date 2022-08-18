#import the argv (arguments) module from the sys package
from sys import argv

#unpack the arg module to have two arguments the first of which is the scriptname and the second is the filename 
script, filename = argv

#open the file and assign it to the variable called txt
txt = open(filename)

#print the name of the opened file
print("Here is your file %r:" % filename)

#read the txt variable and print it to stdout
print(txt.read())

#close the file 
txt.close()

#prompts for the filename again
print("Type the filename again:")

#assign the user input to the variable called file_again
file_again = input("> ")

#open the file and assign it to the txt_again variable
txt_again = open(file_again)

#read and print the file
print(txt_again.read())

#close the file
txt_again.close()