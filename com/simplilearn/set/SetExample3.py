print("This is the SET Example")
print("******** START ***********")

countrySet={"INDIA","US","UK","CHINA","ITLY","INDIA"}
length = len(countrySet)
print(length)#

print("----------------")

countrySet2={"INDIA","US","UK","CHINA","ITLY","INDIA"}
length = len(countrySet)

'''i=0
while (i<=length):
    print(countrySet2[i]) # TypeError: 'set' object is not subscriptable
    i = i+1
'''

print("-START-------FOR LOOP OVER SET--------")

myProgLanguageSet = {"JAVA", "PYTHON", "JSP", "C", "REACT"}

for var3 in myProgLanguageSet:
    print(var3)

print("-END-------FOR LOOP OVER SET--------")



print("******** END ***********")