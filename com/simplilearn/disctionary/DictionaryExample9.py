print("This is the DICTIONARY Example")
print("******** START ***********")
rollDict={
            100:"Iram",
            200:"Mrunal",
            300:"Ankit",
            400:"Suprabha"
        }

print("------------------------------------------------")
print(rollDict)
#print(rollDict[500]) # KeyError: 500

print(rollDict.setdefault(400,"Suprabha")) # Suprabha
print(rollDict.setdefault(400,"Suprabha adhikari")) # Suprabha

print(rollDict)

print(rollDict.setdefault(500,"Vishnu")) #
print(rollDict[500]) #
print(rollDict)

'''
If the key is exist then it returns the corresponding value
    - If you try to set more than one time , 
            -- then the oldest/first value only comes under consideration 
If key does not exist , then a new entry got added in dictionary .

'''
print("******** END ***********")