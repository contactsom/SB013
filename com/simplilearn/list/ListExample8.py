print("This is the LIST By Using For loop Example")
print("******** START ***********")

#(0-6),   (1-6),    (2-6),  (3-6),  (4-6),  (5-6) # (i-x) where i = 0 and x is length = 6
#-6,       -5,        -4,     -3,     -2,     -1  # -ve Index
# A,        B,         C,      D,      E,      F
# 0,        1,         2,      3,      4,      5  # +Ve Index


list=[ "A","B","C","D","E","F" ]

x=len(list)
print(x) # 6

for i in range(x):
    print(list[i],"Is Available at index :",i,"And at the negative index :",i-x)

print("----------------")


print("******** END ***********")