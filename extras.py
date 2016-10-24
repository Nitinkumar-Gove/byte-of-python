
listone = [1,2,3,4,5,6,7,8,9,0]
listtwo = [ 2* item for item in listone if item!=0]

print listone
print listtwo

# -------- decorator -----------
def addtag(tag='none'):
    def decor(func):
        def new_func(text):
            print text + ' <deco> ' + tag
        return new_func
    return decor
    
@addtag()
def show(text):
    print text

show('hi')