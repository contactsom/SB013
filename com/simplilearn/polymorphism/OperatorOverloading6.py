class OperatorOverloading4:
    def __init__(self,name):
        self.name=name

    def __mul__(self, other):
        print(self.name)
        print(other.name)
        return self.name*other.name


o1=OperatorOverloading4(5)
o2=OperatorOverloading4(6)

print(o1*o2) #25