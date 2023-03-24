print("********** This is the Example of File Handling **********")


file=open("data.txt",'r')
print(file.read()) # My Cursor is in Last Line

print("**********************")
file.seek(0) # Reset the cursor : Move the cursor from last line to first line
print(file.read()) #


file.close()