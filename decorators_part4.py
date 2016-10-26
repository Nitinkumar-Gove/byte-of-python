'''
 This program demonstrates decorators and with statement. 
 @author - Nitinkumar Gove
 @version - 1.0 / Oct 25, 2016
'''

def whatever(a,b, *args):                   # function with multiple [variable number of] arguments 
    print a, b, args

def whatever2(**dargs):
    print dargs

whatever(10,20,30,40,50,60,70,80,90,100)
whatever2(a=10, b=20, c=30) 