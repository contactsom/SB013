class Person:
    def __init__(self,name,id,age,address,emailid,gender):
        self.name  = name
        self.id   = id
        self.age  = age
        self.address = address
        self.emailid = emailid
        self.gender = gender


    def getMyDetails(self):
        print("Hello My Name is : ",self.name)
        print("Hello My Id is : ", self.id)
        print("Hello My Age is : ", self.age)
        print("Hello My Address is : ", self.address)
        print("Hello My Email ID is : ", self.emailid)
        print("Hello My Gender is : ", self.gender)

person=Person("Vishal Gupta",101,21,"Bangalore CISCNA Tech park","vishal@simplilearn.com","Male")
person.getMyDetails()