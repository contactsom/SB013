print("********** This is the Example of File Handling **********")

#file=open("abc.txt",'w') # Replace the existing data and write new data on each execution
file=open("abc.txt",'a') # Keep the existing data in to file and write new data on each execution

file.write("********************************** \n")
file.write("I am line 11 \n")
file.write("I am line 21 \n")
file.write("I am line 31 \n")
file.write("I am line 41 \n")
file.write("I am line 51 \n")
file.write("I am line 61 \n")
file.write("********************************** \n")

file.write("I am line 1 \n")
file.write("I am line 2 \n")
file.write("I am line 3 \n")
file.write("I am line 4 \n")
file.write("I am line 5 \n")
file.write("I am line 6 \n")


file.close()

