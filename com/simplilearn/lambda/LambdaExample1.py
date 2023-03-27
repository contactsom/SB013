print("Example without lambda ")

def addTwo(a,b):
    c = a+ b
    return c

result=addTwo(20,30)
print(result)

print("Example with lambda ")

result1=lambda a,b:a+b
print(result1(20,30))

print("------------------------------------")
result2=lambda a,b,c:a+b+c
print(result2(20,30,80))

print("------------------------------------")


square=lambda a : a*a
squreresult=square(4)
print(squreresult)

print("------------------------------------")


biggest=lambda a , b : a if a > b else b
biggestResult=biggest(30,89)
print(biggestResult)




