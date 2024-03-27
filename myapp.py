from fastapi import FastAPI
from fastapi import Path
from typing import Optional
from student import Student
from updatestudent import UpdateStudent

print("Hello World")

app = FastAPI()

@app.get("/")
def home():
    return {"name":"This is my first FastAPI"}

students = {
    1:{
        "name" : "Naga",
        "course" : "FastAPI",
        "age" : 35
    },
    2:{
        "name" : "Ash",
        "course" : "Datascience",
        "age" : 29
    }
}

@app.get("/getstudents")
def get_student():
    return students

@app.get("/getstudent/{student_id}")
def get_student(student_id : int = Path( description="Unique Student ID")):
    print("Received Request "+str(student_id))
    return students.get(student_id)
    
@app.get("/getstudentbynameorcourse")
def get_student_by_name(*, name : str, course: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"]==name or students[student_id]["course"]==course :
            return students[student_id]
    return {name:"not found"}

@app.get("/getstudentbyidandname/{student_id}")
def get_student_byid_and_name(*, student_id : int = Path(description="Unique Student ID"), name : str):
                              
    print("Received Request "+str(student_id)+ " name = "+ name)
    return students.get(student_id)

@app.post("/createstudent/{student_id}")
def create_student(*, student_id : int, student: Student):
    if student_id in students:
        return {student_id : "Student already exists"}
    
    students[student_id] = student
    return students[student_id]

@app.post("/createnewstudent/{student_id}")
def create_new_student(*, student_id : int, student : Student):
    if student_id in students:
        return {student_id : "already present"}
    else:
        students[student_id] = student
        return students[student_id]
    
@app.put("/updatestudent/{student_id}")
def update_student(*, student_id : int , student : UpdateStudent):
    if student_id not in students:
        return {student_id : "Not present"}
    
    if student.name != None:
        students[student_id]["name"] = student.name

    if student.age != None:
        students[student_id]["age"] = student.age

    if student.course != None:
        students[student_id]["course"] = student.course

    return students[student_id]


@app.delete("/deletestudent/{student_id}")
def delete_student(*, student_id : int):
    if student_id not in students:
        return {student_id : "Not present"}
    
    del students[student_id]

    return {student_id : "Deleted Successfully"}

    

        
    
