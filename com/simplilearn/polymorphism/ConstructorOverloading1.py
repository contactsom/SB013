class ConstructorOverloading1:
    def __init__(self):
        print("No Argument Constructor")

    def __init__(self,a):
        print("One Argument Constructor")

    def __init__(self, a,b):
        print("Two Argument Constructor")
#TypeError: ConstructorOverloading1.__init__() missing 2 required positional arguments: 'a' and 'b'
obj1=ConstructorOverloading1()