class MethodOverloading1:

    def m1(self, a, b):
        print("Two Argument Method -2")

    def m1(self):
        print("No Argument Method -0")

    def m1(self,a):
        print("One Argument Method -1")



methodOverloading = MethodOverloading1()

#methodOverloading.m1()
methodOverloading.m1(10)
#methodOverloading.m1(10,20) #methodOverloading.m1(10,20)

'''
TypeError: MethodOverloading1.m1() missing 2 required positional arguments: 'a' and 'b'

TypeError: MethodOverloading1.m1() missing 1 required positional argument: 'b'
'''