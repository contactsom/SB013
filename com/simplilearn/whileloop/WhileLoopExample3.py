print("This is the WHILE LOOP Example")
print("******** START ***********")
mystring = "ABCD"
# 1st Char exist at index 0
# 2nd Char exist at index 1
# 3rd Char exist at index 2
# 4th Char exist at index 3
    # 4th Char exist at index (4-1)
# kth Char exist at index (k-1)

# Length of this string = 4
# Length of this string = (3+1)
# Length of this string = (lastIndex+1)

# last index = length-1
lengthofString=len(mystring)
print(lengthofString)


k=0
while(k<lengthofString):
    print(mystring[k])
    if(mystring[k]=='C'):
        print("Character C found at index :",k)
        break
    k=k+1
print("I am done")


print("******** END ***********")