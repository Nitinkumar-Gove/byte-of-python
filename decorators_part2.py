
'''
 This program demonstrates decorators and with statement. 
 @author - Nitinkumar Gove
 @version - 1.0 / Oct 25, 2016
'''

def wrapper(func):                 # decorate the function and return new one
    
    def new_wrapper():
        print 'v2.0'
        x = func() 
        print x + 10

    return new_wrapper 

def simple():
    return 5

print 'simple() v1.0 - ', simple()
simple = wrapper(simple)         # fetch the decorated version of simple()
simple()