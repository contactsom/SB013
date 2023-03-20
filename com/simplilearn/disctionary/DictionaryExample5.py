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

del rollDict[100]
del rollDict[200]
del rollDict[300]
del rollDict[400]
print("******* After Delete ********")
print(rollDict) #{}

print("----------------------------------------------------------------")
print("-----------------------------clear()-----------------------------------")
rollDict1={
            100:"Iram",
            200:"Mrunal",
            300:"Ankit",
            400:"Suprabha"
        }

print("******* Before Clear ********")
print(rollDict1)

rollDict1.clear()

print("******* After Clear ********")
print(rollDict1) #{}

#  Dictionary Exist with no data - Empty Dictionary


print("******** END ***********")