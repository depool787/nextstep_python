student= []

student1={
    "name":"alice",
    "age":16,
    "major":"math",
}
student2={
    "name":"bob",
    "age": 19,
    "major": "social",    
}

student.append(student1)
student.append(student2)

for student in student:
    print(f"name ->{student['name']} age -> {student['age']} major -> {student['major']}")
