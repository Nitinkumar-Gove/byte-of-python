
'''
This program demonstrates data structures in python and related concepts
@author - Nitinkumar Gove
@Verstion - V1.0 / 23 Oct 2016
'''
#a simple list of string objects
to_do = ['call mhatre', 'cook sabji', 'finish async example']

def printlist(lst):
    for item in lst:
        print item

print len(to_do)

#prinint list item by item
printlist(to_do)

#adding new items to list
to_do.append('wash clothes')
to_do.append('iron clothes')

#sorting list items
to_do.sort()

print "\n\n --- sorted to do list -----"
printlist(to_do)

#delete item from list
del to_do[3]
printlist(to_do)

# *** TUPLES ***

bag = 'pen','pencil','notebook'
print bag

put_in_bag = 'books','bottle'

full_bag = bag, put_in_bag

print full_bag[1]

# *** DICTIONARY ***

expenses = {
    'aug': 600,
    'sep': 540,
    'oct': 550,
    'nov': 640
}

print expenses['nov']

expenses['dec'] = 230                                   # adding new values to the dictionary 
expenses['jan'] = 300
expenses['feb'] = 400

print expenses

del expenses['aug']

for month, exp in expenses.items():                     # items() returns the key-value pairs in dictionary
    print 'you spent ${0} in {1}'.format(exp,month)

if 'aug' in expenses:                                   # in operator is used to find key in dictionary
    print expenses['aug']
else:
    print 'not found'

# *** SETs ***

countries = set(['india','srilanka','nepal','south africa'])
if 'india' in countries:
    print 'found'

set2 = countries.copy()
print set2

set2.add('usa')
set2.add('mexico')
print set2