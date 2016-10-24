'''
This program demonstrates pickle in python and related concepts
@author - Nitinkumar Gove
@Verstion - V1.0 / 24 Oct 2016
'''
import pickle

datafile = 'data.txt'
to_do = ['call mom','solve atm problem','make video', 'show the plan']

# write in 'binary' mode to a file
fref = open(datafile, 'wb')         # file is  created, if it doesn't already exist
pickle.dump(to_do,fref)
fref.close()

del to_do                          # delete the object 

fref = open(datafile, 'rb')        # read binary file and store the record in variable
to_do = pickle.load(fref)
print to_do
fref.close()

