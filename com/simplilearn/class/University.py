class University:
    def __init__(self):
        self.uni_name="JNU"
        self.uni_address="South West Delhi,India"
        self.uni_zip=110067

    def display(self):
        print("University Name : ",    self.uni_name)
        print("University Address : ", self.uni_address)
        print("University Zip : ",     self.uni_zip)


university=University()
university.display()

print("***************")
# Getting the data from constructor
print("University Name : ",    university.uni_name)
print("University Address : ", university.uni_address)
print("University Zip : ",     university.uni_zip)