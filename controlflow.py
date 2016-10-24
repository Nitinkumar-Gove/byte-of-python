'''
This program demonstrates simple control flows in python and related concepts
@author - Nitinkumar Gove
@Verstion - V1.0 / 23 Oct 2016
'''

__version__ = 1.0

grade = input('enter your grade') # input() - used to take user input
print grade

if grade < 4.0 and grade > 3.5 :                   # if-else statement
    print '#top performer !'
elif grade < 3.5 and grade > 3.0 :                 # NOTE : How else-if is written in python
    print '#great performer !'
else:
    print '#you better study !'

while grade>0:
    print '#awesome'
    grade -= 1                                     # short assignments

for i in range(1,5):                               # range() function generates s series of numbers (one at a time ) between given two no.s
    print i
    if i == 4:
        break;                                     # break - statement is used to break loops and exit out of it
else:
    print 'loop\'s over !'                         # LOOPS HAVE ELSE *

