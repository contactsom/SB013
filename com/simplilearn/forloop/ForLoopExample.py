print("This is the If elif Else Condition Example")
print("******** START ***********")

x = 10
print(x)

print("-START-------FOR LOOP OVER LIST--------")
# list, tuple, sets, dict
myProgLanguage=["JAVA","PYTHON","JSP","C","REACT"]
               #
# 1st Element is stored at Index 0
# 2nd Element is stored at Index 1
# 3rd Element is stored at Index 2
# 4th Element is stored at Index 3
# 5th Element is stored at Index 4
    # 5th Element is stored at Index (5-1)
# kth Element is stored at Index (k-1)
# Length = 5
# Length = 4+1
# Length = (lastIndex+1)

print(myProgLanguage)
print("----------------")
print(myProgLanguage[0])
print(myProgLanguage[1])
print(myProgLanguage[2])
print(myProgLanguage[3])
print(myProgLanguage[4])

print("----------------")

for var1 in myProgLanguage:
    print(var1)

print("-END-------FOR LOOP OVER LIST--------")

print("-START-------FOR LOOP OVER TUPLE--------")

myProgLanguageTuple=("JAVA","PYTHON","JSP","C","REACT")

for var2 in myProgLanguageTuple:
    print(var2)

print("-END-------FOR LOOP OVER TUPLE--------")

print("-START-------FOR LOOP OVER SET--------")

myProgLanguageSet = {"JAVA", "PYTHON", "JSP", "C", "REACT"}

for var3 in myProgLanguageSet:
    print(var3)

print("-END-------FOR LOOP OVER SET--------")


print("-START-------FOR LOOP OVER DICTIONARY--------")
# k=int,v=String
stuRoll={
        1:"Suprabha",
        2:"Anusha",
        3:"Abhishek",
        4:"Ankit",
        5:"Vishal",
        6:"Dewansh",
        7:"Ankit"
}

print("******** Get the key from the DICTIONARY ******** ")
for var4 in stuRoll:
    print(var4)

print("******** Get the Value from the DICTIONARY ******** ")
for var5 in stuRoll:
    print(stuRoll[var5])


print("******** Get the key,Value from the DICTIONARY ******** ")
for key,value in stuRoll.items():
    print(key,value)

print("-END-------FOR LOOP OVER DICTIONARY--------")


print("-START-------FOR LOOP OVER STRING--------")

# String is a combination of character/space -> Agree
# String holds more than one character  -> Agree
# Hence for loop required to fetch the data  -> Agree
# What is data in String   character/space -> Agree

str1="ABHISHEK KUMAR"
print(str1)
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])
print(str1[6])
print(str1[7])
print(str1[8])
print(str1[9])
print(str1[10])
print(str1[11])
print(str1[12])
print(str1[13])

print("******************")

for s1 in str1:
    print(s1)





print("-END-------FOR LOOP OVER STRING--------")


print("******** END ***********")