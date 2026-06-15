from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.post("/sri")
def greet():
    return "Hello, World!"

@app.post("/greet_name")
def greet_name(name: str):
    return f"Hello, {name}!"

@app.post("/sum_numbers")
def sum_numbers(a: int, b: int):
    return {"sum": a + b}


# Pydantic Model
class StudentRequest(BaseModel):
    name: str
    age: int
    city: str

# POST API
@app.post("/student-info")
def student_info(student: StudentRequest):
    print(f"Name: {student.name}, Age: {student.age}, City: {student.city}")
    return {
        "name": student.name,
        "age": student.age,
        "city": student.city
    }