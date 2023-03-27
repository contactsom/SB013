from functools import *

print("******* Reduce Example *******")

mylist=[1,9,4,8,5]

result1=reduce(lambda a , b : a+b , mylist) # 27
print(result1)


result2=reduce(lambda a , b : a*b , mylist) # 27
print(result2)


result3=reduce(lambda a , b : a*b , range(1,100)) #
print(result3)


result4=reduce(lambda a , b : a+b , range(1,100)) # 4950
print(result4)