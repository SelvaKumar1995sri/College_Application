import uvicorn
from fastapi import FastAPI

import sys

from generate_id import get_latest_student_id, get_latest_faculty_id, get_latest_course_id
from db import get_course_collection, get_faculty_collection, get_student_collection
from basemodel import Courses, Student, Faculty, StudentList,CourseList


app = FastAPI()

def course_serialize_list(course_list):
    return [course.dict() for course in course_list]

@app.get('/api/viewallcourse', tags=['Course'])
def view_all_course():
    try:

        col = get_course_collection()
        course_list = list(col.find({}, {"_id": 0}))
        return {"data": course_list}

    except Exception as e:
        print("error on viewing list " + str(e))


@app.get('/api/viewcourse', tags=['Course'])
def view_course(course_id):
    try:

        col = get_course_collection()
        course = col.find_one({"courseID": course_id}, {"_id": 0})
        return {"data": course}

    except Exception as e:
        print("error on viewing data " + str(e))


@app.post('/api/addcourse', tags=['Course'])
def add_course(course: Courses):
    try:

        col = get_course_collection()
        dict_course = course.dict()
        dict_course['courseID'] = get_latest_course_id()
        col.insert_one(dict_course)
        return {"data": "Successfully added"}

    except Exception as e:
        print("error on adding data " + str(e))

# @app.post('/api/addcourselist', tags=['Course'])
# def add_course_list(course: CourseList):
#     try:

#         col = get_course_collection()
#         dict_course = course
#         print(type(dict_course))
#         dict_course['courseID'] = get_latest_course_id()
#         course_list = course_serialize_list(dict_course)
#         print(type(course_list))
#         col.insert_many(course_list)
#         return {"data": "Successfully added list"}

#     except Exception as e:
#         print("error on adding list " + str(e))

@app.put('/api/updatecourse', tags=['Course'])
def update_course(courseid,course: Courses):
    try:

        col = get_course_collection()
        dict_course = course.dict()
        dict_course['courseID'] = get_latest_course_id()
        col.update_one({"courseID": int(courseid)}, {"$set": course.dict()})
        return {"data": "Successfully updated"}

    except Exception as e:
        print("error on updating data " + str(e))

@app.delete('/api/deletecourse', tags=['Course'])
def delete_course(CourseID):
    try:

        col_c = get_course_collection()
        col_c.delete_one({"courseID": int(CourseID)})
        return {"data": "Successfully added"}

    except Exception as e:
        print("error on deleting data " + str(e))


def student_serialize_list(student_list):
    return [student.dict() for student in student_list]


@app.get('/api/viewallstudent', tags=['Student'])
def view_all_student():
    try:

        col = get_student_collection()
        student_list = list(col.find({}, {"_id": 0}))
        return {"data": student_list}

    except Exception as e:
        print("error on viewing data " + str(e))


@app.get('/api/viewstudent', tags=['Student'])
def view_student(studentid):
    try:

        col = get_student_collection()
        student = col.find_one({"Student_id": int(studentid)}, {"_id": 0})
        return {"data": student}

    except Exception as e:
        print("error on viewing data " + str(e))


@app.post('/api/addstudent', tags=['Student'])
def add_student(student: Student):
    try:

        collection_stu = get_student_collection()
        collection_cor = get_course_collection()
        dict_student = student.dict()
        dict_student['Student_id'] = get_latest_student_id()
        stu_course = dict_student['Course']
        course_id = collection_cor.find_one({"course_name": stu_course})
        dict_student['Course'] = course_id['courseID']
        collection_stu.insert_one(dict_student)
        return {"data": "Successfully added"}

    except Exception as e:
        print("error on adding data " + str(e))

@app.put('/api/updatestudent', tags=['Student'])
def update_student(studentid,student: Student):
    try:

        col = get_student_collection()
        collection_cor = get_course_collection()
        dict_student = student.dict()
        dict_student['Student_id'] = get_latest_student_id()
        stu_course = dict_student['Course']
        course_id = collection_cor.find_one({"course_name": stu_course})
        dict_student['Course'] = course_id['courseID']
        col.update_one({"courseID": int(studentid)}, {"$set": dict_student})
        return {"data": "Successfully updated"}

    except Exception as e:
        print("error on updating data " + str(e))

# @app.post('/api/addstudentlist', tags=['Student'])
# def add_student_list(student: StudentList):
#     try:
#         collection_stu = get_student_collection()
#         collection_cor = get_course_collection()
#         dict_student = student.dict()
#         dict_student['Student_id'] = get_latest_student_id()
#         stu_course = dict_student['Course']
#         course_id = collection_cor.find_one({"course_name": stu_course})
#         dict_student['Course'] = course_id['courseID']
#         student_list = student_serialize_list(dict_student.data)
#         collection_stu.insert_many(student_list)
#         return {"data": "Successfully added list"}

#     except Exception as e:
#          print("error on adding data " + str(e))


@app.delete('/api/deletestudent', tags=['Student'])
def delete_student(student_id):
    try:

        col = get_student_collection()
        col.delete_one({"Student_id": student_id})

        return {"data": "Successfully deleted"}

    except Exception as e:
        print("error on adding data " + str(e))


@app.get('/api/viewallfaculty', tags=['Faculty'])
def view_all_faculty():
    try:

        col = get_faculty_collection()
        faculty_list = list(col.find({}, {"_id": 0}))
        return {"data": faculty_list}

    except Exception as e:
        print("error on viewing data " + str(e))


@app.get('/api/viewfaculty', tags=['Faculty'])
def view_faculty(facultyid):
    try:

        col = get_faculty_collection()
        faculty = col.find_one({"faculty_id": int(facultyid)}, {"_id": 0})
        return {"data": faculty}

    except Exception as e:
        print("error on viewing data " + str(e))


@app.post('/api/addfaculty', tags=['Faculty'])
def add_faculty(faculty: Faculty):
    try:

        col = get_faculty_collection()
        collection_cor = get_course_collection()
        dict_faculty = faculty.dict()
        dict_faculty['faculty_id'] = get_latest_faculty_id()
        course_id = collection_cor.find_one(
            {"course_name": dict_faculty['Course']})
        dict_faculty['Course'] = course_id['courseID']
        col.insert_one(dict_faculty)
        return {"data": "Successfully added"}

    except Exception as e:
        print("error on adding data " + str(e))


@app.delete('/api/deletefaculty', tags=['Faculty'])
def delete_faculty(faculty_id):
    try:

        col = get_faculty_collection()
        col.delete_one({"faculty_id": faculty_id})

        return {"data": "Successfully deleted"}

    except Exception as e:
        print("error on adding data " + str(e))


@app.get('/api/view_class_student_&_faculty', tags=['Class'])
def view_class(course_name):
    try:

        collection_course = get_course_collection()
        collection_student = get_student_collection()
        collection_faculty = get_faculty_collection()
        course_element = collection_course.find_one(
            {"course_name": str(course_name)})
        faculty_list = list(collection_faculty.find(
            {"Course": course_element['courseID']}, {"_id": 0}))
        student_list = list(collection_student.find(
            {"Course": course_element['courseID']}, {"_id": 0}))

        return {"faculty for this class": faculty_list, "students": student_list}

    except Exception as e:
        print("error on viewing data " + str(e))

@app.get('/api/view_student_academic_year', tags=['Class'])
def view_academic_year(year):
    try:
        l=[]
        collection_student = get_student_collection()
        student_list = collection_student.find({},{"_id":0})
        if student_list['Joining_Date'].endswith(year):
            l.append(student_list)

        return {"students":l}

    except Exception as e:
        print("error on viewing data " + str(e))


if __name__ == '__main__':
    uvicorn.run("app:app", reload=True, access_log=False)
