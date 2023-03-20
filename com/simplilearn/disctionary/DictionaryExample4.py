print("This is the DICTIONARY Example")
print("******** START ***********")
rollDict={
            100:"Iram",
            200:"Mrunal",
            300:"Ankit",
            400:"Suprabha"
        }
print("----------------")
# how to delete the dictionary Value
print("******* Before Delete ********")
print(rollDict)

del rollDict[200]
print("******* After Delete ********")
print(rollDict)
print("----------------------------------------------------------------")
print("----------------------------------------------------------------")

#del rollDict[800] #KeyError: 800
if 800 in rollDict:
    del rollDict[800]
else:
    print("Can not be deleted as Key not exist")

print("----------------")
print("******** END ***********")