'''
This program demonstrates functions in python and related concepts
@author - Nitinkumar Gove
@Verstion - V1.0 / 23 Oct 2016
'''

__version__ = 1.0

#simple function
def get_max(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return None

#default values , check y 
def raiseto(x, y=1):
    return x**y

#var args
def printall(*numbers):
    for i in numbers:
        print i

a = 10 
b = 10
print get_max(a,b)

print raiseto(a)                         # you can skip variables which have default values
print raiseto(a,2)

printall(1,2,3,4,5,6,7,8,9,0)