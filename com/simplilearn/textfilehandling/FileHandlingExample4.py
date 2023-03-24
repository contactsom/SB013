print("********** This is the Example of File Handling **********")

file=open("mylist.txt",'a') # Keep the existing data in to file and write new data on each execution

list=["A\n","B\n","C\n","D\n","E\n","F\n","G\n"]

file.writelines(list)


file.close()

