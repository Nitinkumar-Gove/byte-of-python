'''
This program demonstrates classes in python and related concepts
@author - Nitinkumar Gove
@Verstion - V1.0 / 24 Oct 2016

'''

class school:

    def __init__(self,sname):
        self.sname = sname

class student(school):

    def __init__(self,sname, name):            #constructor
        school.__init__(self, sname)
        self.name = name

    @classmethod                               #class method
    def justmsg(self):
        print 'this is class method'


    def printinfo(self):                       #object method
        print 'name : ',self.name
        print 'school name :',self.sname

s = student('ATZ','nitin')
s.printinfo()
student.justmsg()