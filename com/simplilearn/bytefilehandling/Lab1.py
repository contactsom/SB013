print("************** START-Byte FIle Handling **************")

inputfile=open("simplilearn-logo.jpg",'rb')
outputfile=open("new_simplilearn-logo.jpg",'wb')

inputfileBytes=inputfile.read()

outputfile.write(inputfileBytes) # Writing the byte data

print("************** New Image File  Created **************")


print("************** END-Byte FIle Handling **************")