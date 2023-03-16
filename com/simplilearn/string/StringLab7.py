print("This is the String Example")
print("******** START ***********")

simplilearnStr1="Simplilearn provides World’s #1 Online Bootcamp"
print(simplilearnStr1)

print("-------***************************************---------")


print('Simplilearn provides World’s # %(rank)d Online Bootcamp'
      %{"rank":1}
      )

print('Simplilearn provides World’s # %(rank)d Online Bootcamp'
      %{"rank":2}
      )

# Simplilearn is INDIA No 1 PYTHON Training Online Bootcamp.


print("-------***************************************---------")

print('%(edtech)s is %(country)s No %(rank)d %(course)s Training Online Bootcamp'
      %{
        "edtech":"Simplilearn",
        "country":"INDIA",
        "rank":1,
        "course":"PYTHON",
        }
      )

# Home Work
# Replace all the value enclosed with () dynamically
''' 
Simplilearn World’s #1 Online Bootcamp. 5,000,000 careers advanced 1,500 live classes every month.
85% report career benefits including promotion or a new job
'''

''' 
(Simplilearn) World’s (#1) Online Bootcamp. (5,000,000) careers advanced (1,500) live classes every month.
(85%) report career benefits including (promotion) or a new job
'''

print("******** END ***********")






