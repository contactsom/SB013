print("********** This is the Example of File Handling **********")

file=open("book.txt",'r')

data=file.read(10) # First 10 Characters
print(data) # I am line

file.close()

