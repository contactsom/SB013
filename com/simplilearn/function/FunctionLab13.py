print("This is the Function Example")
print("******** START ***********")

def getSumSub(a,b):
    sum=a+b
    sub=a-b
    mul= a * b
    div=a/b
    return sum,sub,mul,div


result1= getSumSub(40,10)
print(result1)

print("-----------------------")
sumResult,subResult,mulResult,divResult= getSumSub(40,10)
print(sumResult)
print(subResult)
print(mulResult)
print(divResult)


print("******** END ***********")

