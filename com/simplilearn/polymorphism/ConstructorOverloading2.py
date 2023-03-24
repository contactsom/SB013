class ConstructorOverloading1:
    def __init__(self,a=None,b=None,c=None):
        print("Constructor with 0 , 1, 2, 3 Number of Argument")

obj1=ConstructorOverloading1()
obj2=ConstructorOverloading1(2)
obj3=ConstructorOverloading1(1,2)
obj4=ConstructorOverloading1(1,2,3)
#obj5=ConstructorOverloading1(1,2,3,4)