from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {"name": "John", "age": 17, "class": "Year 12"},
    2: {"name": "Jane", "age": 16, "class": "Year 11"},
}


class Student(BaseModel):
    name: str
    age: int
    year: int


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(
        ..., description="The ID of the student you want to view", gt=0, lt=3
    )
):
    return students[student_id]


@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Data": "Student already exists"}

    students[student_id] = student
    return students[student_id]
