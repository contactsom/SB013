
try:
    x = int(input("Enter the First Number : "))
    y = int(input("Enter the Second Number : "))
    print(x/y)
except ZeroDivisionError as msg:
    print("Can not devide any number by Zero - ", msg)
except ValueError as msg1:
    print("We expect only number as Input - ", msg1)