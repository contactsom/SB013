print("This is the DICTIONARY Example")
print("******** START ***********")
rollDict={
            100:"Iram",
            200:"Mrunal",
            300:"Ankit",
            400:"Suprabha"
        }

#print(rollDict)
print("----------------")
print(rollDict[100])
print(rollDict[200])
print(rollDict[300])
print(rollDict[400])
    #print(rollDict[500]) #KeyError: 500

print("----------------")
#rollDict.hash_key(500) # This function exist in python 2 not python 3

print("----------------")

if 200 in rollDict:
    print(rollDict[200])
else:
    print("Key-200 Not Exist")

print("----------------")

if 201 in rollDict:
    print(rollDict[200])
else:
    print("Key-200 Not Exist")

print("******** END ***********")