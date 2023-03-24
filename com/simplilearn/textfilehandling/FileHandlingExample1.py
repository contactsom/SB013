print("********** This is the Example of File Handling **********")

file=open("pogo.txt",'w')

print("File Name : ",file.name)
print("File Mode : ",file.mode)
print("Is this File in redable Mode : ",file.readable())
print("Is this File in writable Mode : ",file.writable())
print("Is this File in Closed : ",file.closed)

file.close()

print("Is this File in Closed : ",file.closed)