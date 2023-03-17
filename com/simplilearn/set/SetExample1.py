print("This is the SET Example")
print("******** START ***********")

countrySet={"INDIA","US","UK","CHINA","ITLY"}
print(countrySet)
print(type(countrySet)) # <class 'set'>

print("----------------")

countryList=["INDIA","US","UK","CHINA","ITLY"]
print(type(countryList)) # <class 'list'>
print(countryList) #

countrylist=set(countryList)
print(type(countrylist)) # <class 'set'>
print(countrylist) #

print("----------------")

mySet=set(range(5))
print(mySet)
print(type(mySet))

print("----------------")

mySet1=set(range(0,19))
print(mySet1)
print(type(mySet1))

print("----------------")

mySet2=set(range(0,19,2))
print(mySet2)
print(type(mySet2))


print("----------------")

mySet3={}
print(mySet3)
print(type(mySet3)) #<class 'dict'>

print("----------------")

mySet4=set()
print(mySet4)
print(type(mySet4)) #<class 'set'>


print("******** END ***********")