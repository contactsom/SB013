print("This is the SET Example")
print("******** START ***********")

x ={10,20,30,40}
y ={30,40,50,60}

print(x.union(y)) # {40, 10, 50, 20, 60, 30}

print("----------------")

x ={10,20,30,40}
y ={30,40,50,60}

print(x|y) # {40, 10, 50, 20, 60, 30}

print("----------------")

mySet={1,2,3,4}
mySet.add(40)
print(mySet)

print("----------------")

x1 ={10,20,30,40}
y1 ={30,40,50,60}

print(x1.intersection(y1)) # {40,30}


print("----------------")

x2 ={10,20,30,40}
y2 ={30,40,50,60}

print(x2.difference(y2)) # {10, 20}


print("----------------")

x3 ={10,20,30,40}
y3 ={30,40,50,60}

print(x3.symmetric_difference(y3)) # {10, 50, 20, 60}

print("******** END ***********")