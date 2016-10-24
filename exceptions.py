
'''
This program demonstrates exceptions in python and related concepts
@author - Nitinkumar Gove
@Verstion - V1.0 / 24 Oct 2016
'''
import logging

# configure logging here
log_file = 'log.txt'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=log_file,
    filemode='w',
)

logging.debug("Start of the program")

# define exception class
class ShortNameException(Exception):
    def __init__(self, name, length):
        Exception.__init__(self)
        self.name = name
        self.length = length

# main logic
try:
    name = raw_input('enter your name - ')    
    logging.info("Checking user input")
    if len(name)<2:
        raise ShortNameException(name, len(name))
except NameError:
    print 'Error : Use raw_input() method instead'
except ShortNameException as e:
    logging.error('Name too short')
    print 'Error : Name too short'