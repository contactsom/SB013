print("******* Map Example *******")


mylist=[2,4,3,6,9,10] # 6
def doubleMe(mylist):
    return mylist*2
print(mylist)

# I want to double all the list element

doubleResut=list(map(doubleMe,mylist))
print(doubleResut)


print("_________________________________")

'''
List of employee salary [100 Employee]
1. Find the top five employee salary : filter
2. To increase all the employee salary  by 10 % : map


'''

list1=[1,5,2,7,9,12]

revisedSalery=list(map(lambda x :2*x,list1))
print(revisedSalery)














