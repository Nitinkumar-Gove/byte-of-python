'''
This program demonstrates functions in python and related concepts
@author - Nitinkumar Gove
@Verstion - V1.0 / 23 Oct 2016
'''

import sys
import functions

__version__ = 1.0

functions.get_max(10,20)                # this function is imported from functions.py module in this directory

#print command line arguments
for a in sys.argv:
    print a

for p in sys.path:
    print p

print __name__

print dir

print dir(sys)

'''
Never user 'from sys import path' i.e 'from' statement because this might lead to variable name conflicts
in your program. Dont rely on implicit, specify everything explicitely.

'''