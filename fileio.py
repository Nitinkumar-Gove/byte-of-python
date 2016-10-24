'''
This program demonstrates files I/O in python and related concepts
@author - Nitinkumar Gove
@Verstion - V1.0 / 24 Oct 2016
'''
# function reverse a string
def reverse_string(string):
    return string[::-1]

#function to check if the string is palindrome string
def check_palindrome(n):
    tmp = reverse_string(n)
    return n == tmp

# get user input 
name = raw_input('enter your name -')
print check_palindrome(name)

# ------- read file -----------

f = open('oops.py')                 # open file in 'r' mode
while True:
    line = f.readline() 
    if len(line) == 0:
        break
    print (line)

f.close()                           # close file

f  = open('oops.py', 'a')           # open file in 'a' append mode
f.write('#test - file write - from [ fileio.py ]')
f.close()