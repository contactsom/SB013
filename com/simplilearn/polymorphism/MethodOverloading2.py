class MethodOverloading2:
    def getSum(self,a=None,b=None,c=None):

        if(a!=None and b!=None and c!=None):
            print("Sum of Three Number is ", a+b+c)
        elif(a!=None and b!=None ):
            print("Sum of Two Number is ", a + b)
        elif (a!= None):
            print("Sum of One Number is ", a)
        else:
            print("Please provide at least one Number to get the Sum ")

o1=MethodOverloading2()
o1.getSum() # Please provide at least one Number to get the Sum
o1.getSum(1) # Sum of One Number is  1
o1.getSum(1,2) # Sum of Two Number is  3
o1.getSum(1,2,3) # Sum of Three Number is  6