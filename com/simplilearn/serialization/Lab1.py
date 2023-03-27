import pickle

teacherdata ={
        "NAME"  :"Kunal",
        "PHONE" :"98657135",
        "EMIAL" :"kunal@simplilearn.com",
        "DOMAIN" :"IT",
        "PASSWORF" :"impassword"
}

#  Serialization
with open("teacher.pickle",'wb') as writefile:
    pickle.dump(teacherdata,writefile)
print("Writing the Oject in to file teacher.pickle ",teacherdata)

#  De-Serialization
with open("teacher.pickle",'rb') as readfile:
    teacherdata_Byte=pickle.load(readfile)
print("Reading the Oject from the file teacher.pickle ",teacherdata_Byte)


if teacherdata == teacherdata_Byte:
    print("Serialization and De-Serialization successfull")
else:
    print("Serialization and De-Serialization NOT successfull")







