print("This is the Exception Handling Example")
print("******** START ***********")

print("Statement 1")
try:
    print("Statement 2")
    print(10/5)
    print("Statement 3")
except ZeroDivisionError:
    print("Statement 4")
    print(10/2)
    print("Statement 5")
print("Statement 6")




print("----------------")
print("******** END ***********")