import csv

teachesrData=[
            ["NAME","EMAIL","PHONE"],
            ["Vishal","vishal@simplilearn.com","9876134"],
            ["Asha", "asha@simplilearn.com", "9512134"],
            ["Suprabha", "suprabha@simplilearn.com", "2112134"]
            ]

with open('teacher.csv',mode='w') as file:
    writer=csv.writer(file)

    for i in teachesrData:
        writer.writerow(i)


