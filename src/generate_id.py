c_id = 9800
s_id = 202200
f_id = 202299

def get_latest_course_id():
    global c_id
    c_id += 1
    return c_id

def get_latest_student_id():
    global s_id
    s_id += 1
    return s_id

def get_latest_faculty_id():
    global f_id
    f_id += 1
    return f_id
