print("This is the LIST Example")
print("******** START ***********")


mylist1=list(range(0,10))
print(mylist1) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("----------------")

mylist2=list(range(0,10,2))
print(mylist2) # [0, 2, 4, 6, 8]


print("----------------")

mylist3=list(range(0,12,3))
print(mylist3) # [0, 3, 6, 9]

print("----------------")

myName="asha jyoti"
l=list(myName)
print(l)


print("----------------")

SimplilearnStr="The Power of Simplilearn's Bootcamp"
SimplilearWord=SimplilearnStr.split()
print(SimplilearWord) # List of Word
l1=list(SimplilearWord) # Explictely Converting a List of Word
print(l1)



print("******** END ***********")