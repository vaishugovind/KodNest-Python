# write a student profile class , objects of that class should have following attributes
# student_name-->string
# student_id-->int
# student_email-->email_id
# student_course-->string
# student_skills-->list of skills
# after creating class create 3 student objects with proper data

def __init__ (self, student_name, student_id, student_email, student_course, student_skills ):
    self.student_name=student_name
    self.student_id=student_id
    self.student_email=student_email
    self.student_course=student_course
    self.student_skills=student_skills

def display_info(self):
    print("Student Name: ", self.student_name)
    print("Student ID: ", self.student_id)
    print("Student Email: ", self.student_email)
    print("Student Course: ", self.student_course)
    print("Student Skills: ", self.student_skills)

# creating 3 objects student
student_profile = None
st1=student_profile("vaishu", 1, "[]", "Computer Science", ["python", "java"])
st2=student_profile("giri", 2, "[]", "Computer Science", ["python", "java"])
st3=student_profile("rishu", 3, "[]", "Computer Science", ["python", "java"])

st1.display_info()
st2.display_info()
st3.display_info()


    
     

    