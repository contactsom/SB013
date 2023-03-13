print("This is the Floor Division Operators Types Example")
print("******** START ***********")

print("------ Case 1: Where m & n tends to +infinity than it returns q ------")

m = 4
n = 2
mn=m//n
print(mn) # 2

print("----------------")

x = 20
y = 10
xy=x//y
print(xy) # 2

print("----------------")

x1 = 20.0
y1 = 10
z1 = x1//y1
print(type(z1)) #
print(z1)


print("------ Case 2: Where m or n (not m and n) tends to -infinity & r=0 (perfectly divisible) than it returns -(q). ------")

a1 = -4
b1 = 2
c1 = a1//b1
print(c1)

print("----------------")

a2 = 6
b2 = -3
c2 = a2//b2
print(c2) # -2

print("----------------")

a3 = 11
b3 = -1
c3 = a3//b3
print(c3) # -11


print("------ Case 3: Where m or n (not m and n) tends to -infinity and r!=0 (NOT perfectly divisible) than it returns -(q+1). ------")

a4 = 11
b4 = -2
c4 = a4//b4
print(c4) # -(5+1) = -6

print("----------------")

a5 = -90
b5 = 4
c5 = a5//b5
print(c5) # -(22+1) = -23



print("******** END ***********")