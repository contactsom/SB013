class Employee:
    def __init__(self):
        self.name="Golagana"
        self.age=33
        self.salary=5000

    def getDetails(self):
        print("Hello I am ",self.name)
        print("Hello I am ", self.age)
        print("Hello I am ", self.salary)

print(Employee.__doc__) ## Description for the class
help(Employee) ## Description for the class

#getDetails()
