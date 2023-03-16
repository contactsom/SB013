print("This is the String for +ve and -ve index Example")
print("******** START ***********")

#ABCDEFGH
# A B C D E F G H
# 0 1 2 3 4 5 6 7

#[m:n]
# m - Start point or FROM
# n - End Point or TO
#[FROM:TO]
# Where n = TO-1
print("--------------------------")
print("+Ve Representaion of Sting")
print("--------------------------")
myString="ABCDEFGH"
print(myString)
print("[1:5] "+myString[1:5]) # B C D E
print("[0:0] "+myString[0:0]) #
print("[0:8] "+myString[0:8]) # A B C D E F G H
print("[0:80] "+myString[0:80]) # A B C D E F G H
print("[0:9] "+myString[0:9]) #A B C D E F G H
print("[:9] "+myString[:9]) #A B C D E F G H
print("[0:] "+myString[0:]) #A B C D E F G H
print("[:] "+myString[:]) #A B C D E F G H
#print("[80] "+myString[80]) # string index out of range

#[m:n:i]
# m - Start point or FROM
# n - End Point or TO
# i - Interval
# [FROM:TO:Interval]

print("[0:5:2] "+myString[0:5:2]) # ACE

# A B C D E
# ACE















print("******** END ***********")






