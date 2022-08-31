import pymongo


client = pymongo.MongoClient(
    "mongodb+srv://gayathri:Sairambaba@cluster1.davwpcs.mongodb.net/?retryWrites=true&w=majority")
mydata = client['college_registry']
student_collection = mydata['student_registry']
course_collection = mydata['course_registry']
faculty_collection = mydata['faculty_registry']

# client = motor.motor_tornado.MotorClient("mongodb+srv://gayathri:Sairambaba@cluster1.davwpcs.mongodb.net/?retryWrites=true&w=majority", serverSelectionTimeoutMS=5000)

def get_course_collection():
    return course_collection

def get_student_collection():
    return student_collection

def get_faculty_collection():
    return faculty_collection

course_list = [
    "bachelor of computer science",
    "bachelor of computer aplication",
    "bachelor of Commerce",
    "Bachelor of Technology",
    "Biotechnology"
]