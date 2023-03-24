print("********** This is the Example of File Handling **********")

with open("employee.txt",'r') as file :
    print(file.read())
    print("Is this File in Closed : ", file.closed) # false
print("Is this File in Closed : ", file.closed) # true One work done your file will get closed automatically


# Is readline method exist in with type also?
# sir what happens if file is not close if we are not using with type

