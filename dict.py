student={
    'name':"jhon the don",
    "age": 25,
    "address":"banepa",
}

student_name=student["name"]
student_age=student.get('age')

student["age"]=20

print(student)

del student["address"]

print(student)


for key,value in student.items():
    print(f"key:{key}-> value:{value}")
    
    
name =["ram","ram"]
name_set={"ram","ram"}





