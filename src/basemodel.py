from pydantic import BaseModel
from typing import List

class Courses(BaseModel):
    courseID : int
    course_name : str
    course_discription : str

class Faculty(BaseModel):
    faculty_id: int
    faculty_name: str
    DOB: str
    gender: str
    Course: str

class Student(BaseModel):
    Student_id: int
    Student_name: str
    DOB: str
    gender: str
    Course: str

class StudentList(BaseModel):
    data: List [ Student ]

class CourseList(BaseModel):
    data: List [ Courses ]