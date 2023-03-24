import json

teacherdata ={
        "NAME"  :"Kunal",
        "PHONE" :"98657135",
        "EMIAL" :"kunal@simplilearn.com",
        "DOMAIN" :"IT",
        "SUBJECT":["JAVA","PYTHON","C","C++"]
}

with open("teachers.json",'w') as file:
   json.dump(teacherdata,file)