class Student:
    def __init__(self, name, rollNo, age, address, emailid, gender,marks,stream,result):
        self.name = name
        self.rollNo = rollNo
        self.age = age
        self.address = address
        self.emailid = emailid
        self.gender = gender
        self.marks = marks
        self.stream = stream
        self.result = result

    def aboutStudent(self):
       print("Student Name : ",self.name)
       print("Student ID : ", self.rollNo)
       print("Student Age : ", self.age)
       print("Student Address : ", self.address)
       print("Student Email ID : ", self.emailid)
       print("Student Gender : ", self.gender)
       print("Student Marks : ", self.marks)
       print("Student Stream : ", self.stream)
       print("Student Result : ", self.result)




student=Student("Suprabha Adhikari", 200, 19, "Delhi NCR", "suprabha.adhikari@simplilearn.com", "Female",90,"Science","Pass")
student.aboutStudent()

print("************************")

student1=Student("Aniket Kumar", 210, 31, "Hyderabad", "aniket.Kumar@simplilearn.com", "Male",80,"Computer Science","Pass")
student1.aboutStudent()