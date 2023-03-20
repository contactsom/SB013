print("This is the Function Example")
print("******** START ***********")
'''
a: first Argument
b: Second Argument
'''

def addTwo(firstNum,secondNum):
    print("What is the First Number :",firstNum)
    print("What is the Second Number :", secondNum)
    totalNum=firstNum+secondNum
    print("What is the Result :", totalNum)
    return totalNum
    #print("I am Done") # Why After return statement no other statement is visible for function


result=addTwo(36,62)
print(result)


print("-----------------------")
print("******** END ***********")