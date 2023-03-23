class OperatorOverloading4:
    def __init__(self,name):
        self.name=name

    def __add__(self, other):
        print(self.name)
        print(other.name)
        return self.name+other.name


o1=OperatorOverloading4("Vishal")
o2=OperatorOverloading4("Gupta")

print(o1+o2) #VishalGupta