print("This is the Tuple Example")
print("******** START ***********")

mydata=[10,2,30] # list
# To convert the list to tuple
myTuple=tuple(mydata)
print(myTuple)
print(type(myTuple))


print("----------------")

myTuple1=tuple(range(0,15))
print(myTuple1)
print(type(myTuple1))

print("----------------")

myTuple2=tuple(range(0,15,2))
print(myTuple2)
print(type(myTuple2))


print("******** END ***********")