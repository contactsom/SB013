print("This is the DICTIONARY Example")
print("******** START ***********")
rollDict={
            100:"Iram",
            200:"Mrunal",
            300:"Ankit",
            400:"Suprabha"
        }

print(rollDict)
print("------------------Key's------------------------------")
print(rollDict.keys()) # dict_keys([100, 200, 300, 400])

print("------------------Values's------------------------------")
print(rollDict.values()) # dict_values(['Iram', 'Mrunal', 'Ankit', 'Suprabha'])

print("------------------Items's------------------------------")
print(rollDict.items()) # dict_items([(100, 'Iram'), (200, 'Mrunal'), (300, 'Ankit'), (400, 'Suprabha')])

print("------------------Copy's------------------------------")
print(rollDict)
newRollDict=rollDict.copy()
print(newRollDict)

print("******** END ***********")