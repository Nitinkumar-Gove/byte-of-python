'''
This program demonstrates simple strings and related concepts
@author - Nitinkumar Gove
@Verstion - V1.0 / 23 Oct 2016
'''

__version__ = 1.0

# defining program variables
goal = 'to become a Millionaire'
deadline = 2020
name = 'Nitin'

# using format() method with strings
print '{0} has a goal which is {1} by {2}'.format(name,goal,deadline)

# multi line strings
print "this is first line .. \
        and this is second"

# raw string - NOTE : raw strings are really useful when used with regular expressions.
raw_string = r'this is a \1 raw string "nothing more"'
print raw_string


