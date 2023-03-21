print("This is the Exception Handling Example")
print("******** START ***********")


try:
    print(10/0)
except ZeroDivisionError:
    print("Any number can not be devide by Zero , So Please find default response")
    print(10/2)

print("----------------")


print("******** END ***********")