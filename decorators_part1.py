'''
 This program demonstrates decorators. 
 @author - Nitinkumar Gove
 @version - 1.0 / Oct 25, 2016
'''

# inner functions 
def update(n):                             # function 1
    
    def square(n):                         # --function 2
        return n**2
    
    def cube(n):                           # --function 3
        return n**3
    
    def apply(func, n):                    # --function 4
        f = func(n)
        return f

    return apply(cube,n)                   # passing function as a parameter

# returning fuction as a value
def getnew(x):                              # function 5   
    def sayhi():
        print x    
    return sayhi

#testbed
n = raw_input('enter any number - ')
print update(int(n))

fnew = getnew(int(1))
fnew()
print fnew.func_closure