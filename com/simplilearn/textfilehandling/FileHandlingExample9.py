print("********** This is the Example of File Handling **********")

with open("employee.txt",'w') as file :
    file.write("Abhishek \n")
    file.write("Ankit \n")
    file.write("Vishal \n")
    file.write("Mohit \n")
    file.write("Iram \n")
    file.write("Anusha \n")
    file.write("Gadenra \n")
    print("Is this File in Closed : ", file.closed) # false
print("Is this File in Closed : ", file.closed) # true



# sir what happens if file is not close if we are not using with type

