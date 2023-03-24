print("********** This is the Example of File Handling **********")

file=open("book.txt",'r')

data=file.read()
print(data)

file.close()

