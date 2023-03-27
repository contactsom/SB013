print("******* Filter Example *******")

def isEven(a):
    if a %2==0:
        return True
    else:
        return False

output1=isEven(4)
print(output1)

output2=isEven(5)
print(output2)

mylist=[1,3,5,7,2,4,8,10]
result=list(filter(isEven,mylist))
print(result) # [2, 4, 8, 10]










