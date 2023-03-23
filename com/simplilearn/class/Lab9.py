import sys

class Test:

    def mydata(self):
        print("I am from Test")

test1=Test() # Object Creation
test2=test1 # Referance
test3=test1
test4=test1
test5=test1
test6=test1
print(sys.getrefcount(test1))
'''
Return the reference count of object.
The count returned is generally one higher than you might expect, 
because it includes the (temporary) reference as an argument to getrefcount().

NOTE : For every object , Python internally maintain one default referance variable self 
6+1= 7
'''



