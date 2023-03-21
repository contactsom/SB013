
try:
   print(10/2) # risky code
except ZeroDivisionError as msg:
    print("Can not devide any number by Zero - ", msg)
finally:
    print("I am finally")