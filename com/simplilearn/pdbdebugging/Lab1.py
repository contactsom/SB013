import pdb

def addition(a,b):
    answer= a + b
    #answer = a * b Error Case
    return answer

pdb.set_trace()

''' Error Case '''
''' x = input("Enter the First Number : ")
y = input("Enter the Second Number : ")
'''


x = int(input("Enter the First Number : "))
y = int(input("Enter the Second Number : "))

sum=addition(x,y)
print(sum)