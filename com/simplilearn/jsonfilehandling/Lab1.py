import json

teacherdata ={
        "NAME"  :"Kunal",
        "PHONE" :"98657135",
        "EMIAL" :"kunal@simplilearn.com",
        "DOMAIN" :"IT"
}

with open("teacher.json",'w') as file:
   json.dump(teacherdata,file)