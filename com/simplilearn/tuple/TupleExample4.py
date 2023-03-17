print("This is the Tuple: Index representation Example")
print("******** START ***********")

#   0,  1,  2,  3,  4 # +Ve representation of Index
#(  10, 20, 30, 40, 50)
#   -5, -4  -3, -2, -1 # -Ve representation of Index

t=(10, 20, 30, 40, 50)
print("[2:5] ",t[2:5]) # (30, 40, 50)
print("[2:500] ",t[2:500]) # (30, 40, 50)
print("[2:] ",t[2:]) # (30, 40, 50)
print("[:4] ",t[:4]) # (10, 20, 30, 40)

print("----------------")
print("[-2:5] ",t[-2:5]) # (40, 50)
print("[-2:-5] ",t[-2:-5]) # ()
print("[-5:-2] ",t[-5:-2]) # (10, 20, 30)

print("----------------")

print("[::2] ",t[::2]) # (10, 30, 50)


print("******** END ***********")