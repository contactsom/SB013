import os

try:
   print(10/2) # risky code
   os._exit(0) # This is the code which is responsible to terminate the code abnormally .
except ZeroDivisionError as msg:
    print("Can not devide any number by Zero - ", msg)
finally:
    print("I am finally")