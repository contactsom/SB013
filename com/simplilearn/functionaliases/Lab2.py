print("This is the Function Example")
print("******** START ***********")

def greetings(name):
    print("Hi", name ,"Good Morning")


wish = greetings # wish is the aliases for greetings function

#greetings("Suprabha")

del greetings # deleting the greetings function

wish("Iram")



print("******** END ***********")