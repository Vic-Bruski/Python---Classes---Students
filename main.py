class student :
    def __init__(self,name,rno):
        self.name = " "
        self.rno = 0

    def readdata(self):
        self.name = raw_input("enter name of the student")
        self.rno = int(raw_input("enter roll no. of the student"))

    def printdata(self):
        print " Name of the student is -" , self.name
        print " Roll no. of the student -" , self.rno

class marks(student):
    def __init__(self,eng,phy,chem,maths,cs):  #eng = English , Phy = Physics , Chem = Chemistry , Cs= Computer Science
        self.eng=0
        self.phy=0
        self.chem=0
        self.maths=0
        self.cs=0

    def __init    

    def printdata1(self):
        print "Marks in English =",self.eng
        print "Marks in Physics =",self.phy
        print "Marks in Chemistry =",self.chem
        print "Marks in Maths =",self.maths
        print "Marks in Computer Science=",self.cs

a=marks(12,13,14,14,30)
print a
