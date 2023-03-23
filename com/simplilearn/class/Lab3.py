class Employee:
    def __init__(self):
        self.name="Golagana"
        self.age=33
        self.salary=5000

    def getDetails(self):
        print("Hello I am ",self.name)
        print("Hello I am ", self.age)
        print("Hello I am ", self.salary)


e1=Employee() # Creating the Object of Employee Class , where "e1" is the object name
e1.getDetails() # Calling the getDetails() with the help of e1 object
