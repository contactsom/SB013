class OperatorOverloading4:
    def __init__(self,name):
        self.name=name

o1=OperatorOverloading4(5)
o2=OperatorOverloading4(5)

print(o1*o2) #TypeError: unsupported operand type(s) for *