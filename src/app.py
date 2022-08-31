import uvicorn
from fastapi import FastAPI

import sys

from generate_id import get_latest_student_id,get_latest_faculty_id,get_latest_course_id
from db import get_course_collection,get_faculty_collection,get_student_collection
from basemodel import Courses,Student,Faculty,StudentList



app = FastAPI()

@app.get('/api/viewcourse', tags=['Course'])
def view_course():
    try:

        col = get_course_collection()
        course_list = list(col.find({},{"_id":0}))
        return {"data":course_list}

    except Exception as e:
        print("error on viewing data " + str(e))

@app.post('/api/addcourse', tags=['Course'])
def add_course(course : Courses):
    try:

        col = get_course_collection()
        dict_course = course.dict()
        dict_course['courseID'] = get_latest_course_id()
        col.insert_one(dict_course)
        return {"data":"Successfully added"}
        
    except Exception as e:
        print("error on adding data " + str(e))
@app.delete('/api/deletecourse', tags=['Course'])
def delete_course(CourseID):
    try:

        col_c = get_course_collection()
        col_c.delete_one({"courseID":int(CourseID)})
        return {"data":"Successfully added"}
        
    except Exception as e:
        print("error on adding data " + str(e))


def student_serialize_list(student_list):
    return [student.dict() for student in student_list]


@app.get('/api/viewstudent', tags=['Student'])
def view_student():
    try:

        col = get_student_collection()
        student_list = list(col.find({},{"_id":0}))
        return {"data":student_list}

    except Exception as e:
        print("error on viewing data " + str(e))

@app.post('/api/addstudent', tags=['Student'])
def add_student(student : Student):
    try:

        collection_stu = get_student_collection()
        collection_cor = get_course_collection()
        dict_student = student.dict()
        dict_student['Student_id'] = get_latest_student_id()
        stu_course = dict_student['Course']
        course_id = collection_cor.find_one({"course_name":stu_course})
        dict_student['Course'] = course_id['courseID']
        collection_stu.insert_one(dict_student)
        return {"data":"Successfully added"}
        
    except Exception as e:
        print("error on adding data " + str(e))

@app.post('/api/addstudentlist', tags=['Student'])
def add_student_list(student : StudentList):
    try:

        col = get_student_collection()
        student_list = student_serialize_list(student.data)
        col.insert_many(student_list)
        return {"data":"Successfully added"}
        
    except Exception as e:
        print("error on adding data " + str(e))

@app.delete('/api/deletestudent', tags=['Student'])
def delete_student(student_id):
    try:

        col = get_student_collection()
        col.delete_one({"Student_id":student_id})

        return {"data":"Successfully deleted"}
        
    except Exception as e:
        print("error on adding data " + str(e))


@app.get('/api/viewfaculty', tags=['Faculty'])
def view_faculty():
    try:

        col = get_faculty_collection()
        faculty_list = list(col.find({},{"_id":0}))
        return {"data":faculty_list}

    except Exception as e:
        print("error on viewing data " + str(e))

@app.post('/api/addfaculty', tags=['Faculty'])
def add_faculty(faculty : Faculty):
    try:

        col = get_faculty_collection()
        collection_cor = get_course_collection()
        dict_faculty = faculty.dict()
        dict_faculty['faculty_id'] = get_latest_faculty_id()
        stu_course = dict_faculty['Course']
        course_id = collection_cor.find_one({"course_name":stu_course})
        dict_faculty['Course'] = course_id['courseID']
        col.insert_one(dict_faculty)
        return {"data":"Successfully added"}
        
    except Exception as e:
        print("error on adding data " + str(e))

@app.delete('/api/deletefaculty', tags=['Faculty'])
def delete_faculty(faculty_id):
    try:

        col = get_faculty_collection()
        col.delete_one({"faculty_id":faculty_id})

        return {"data":"Successfully deleted"}
        
    except Exception as e:
        print("error on adding data " + str(e))

if __name__ == '__main__':
    uvicorn.run("app:app", reload=True, access_log=False)