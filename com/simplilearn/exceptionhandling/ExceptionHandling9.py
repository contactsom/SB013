
try:
    x = int(input("Enter the First Number : "))
    y = int(input("Enter the Second Number : "))
    print(x/y)
except ZeroDivisionError as msg:
    #print("Can not devide any number by Zero")
    print("Can not devide any number by Zero - ", msg)