class Parent:
    def property(self):
        print("***Gold-Land-House-Cash***")

# Inharitance
class Child(Parent):
    def property(self):
        print("Father :Gold-Land-House-Cash"+" "+"SELF:Gold-Land-House-Cash")


child=Child()
child.property()