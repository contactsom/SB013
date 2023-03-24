print("********** This is the Example of File Handling **********")

file=open("data.txt",'r')

#line1=file.readline() # This will read the content line by line
lines=file.readlines()

for line in lines:
    print(line,end='')

file.close()

