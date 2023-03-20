print("This is the DICTIONARY Example")
print("******** START ***********")
rollDict={
            100:"Iram",
            200:"Mrunal",
            300:"Ankit",
            400:"Suprabha"
        }
print("----------------")
print(rollDict)
print(len(rollDict)) # 4

print("----------------")

dictvalue=rollDict.get(400)
print(dictvalue) # Suprabha

print("----------------")

rollDict.pop(400)
print(rollDict) # {100: 'Iram', 200: 'Mrunal', 300: 'Ankit'}

print("----------------")
rollDict1={
            100:"Iram",
            200:"Mrunal",
            300:"Ankit",
            400:"Suprabha"
        }

print("********* Before  popitem()")
print(rollDict1)
items=rollDict1.popitem()
print("********* After  popitem()")
print(items) #(400, 'Suprabha')
print(rollDict1) #{100: 'Iram', 200: 'Mrunal', 300: 'Ankit'}

print("----------------")

print("******** END ***********")