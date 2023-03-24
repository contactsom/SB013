class Parent:
    def property(self):
        print("***FATHER-Gold-Land-House-Cash***")

# Inharitance
class Child(Parent):
    def property(self):
        super().property() # calling teh parent class property() function
        print("SELF:Gold-Land-House-Cash")


child=Child()
child.property()