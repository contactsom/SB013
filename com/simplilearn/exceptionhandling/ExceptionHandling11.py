
try:
   print(10/0) # risky code
   # log out code
except ZeroDivisionError as msg:
    print("Can not devide any number by Zero - ", msg)
    # log out code
finally:
    print("I am finally")
    # log out code