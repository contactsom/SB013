'''

If in class

'''

class Lab5:

    def __init__(self):
        print("I am __init__ default ")

    def __init__(self,aa,bb,cc,dd,ee,ff):
        print("I am __init__")
        self.a = aa
        self.b = bb
        self.c = cc
        self.d = dd
        self.e = ee
        self.f = ff

## How many times constructor getting called
#lab4=Lab5(1,2,3,4,5,6)

lab5=Lab5() # TypeError: Lab5.__init__() missing 6 required positional arguments: 'aa', 'bb', 'cc', 'dd', 'ee', and 'ff'
lab6=Lab5()
lab7=Lab5()

lab4=Lab5(1,2,3,4,5,6)