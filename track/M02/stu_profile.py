# A TRAINER PLATFORM WANTS TO STORE A STUDENT'S PROFILE
class StudentProfile:
    def __init__(self, student_id, student_name, course, score):
        self.student_id=student_id
        self.student_name=student_name
        self.course=course
        self.score=score
    def test_status(self):
        if self.score>=40:
            return "Pass"
        else:
            return "Fail"
    def update_score(self,new_score):
         if new_score>=0 and new_score <=100:
            self.score=new_score
            return self.score
         else:
            return "Invalid Score"
    def get_score(self):
        return f"student score is: {self.score}"
    def get_name(self):
        return f"student name is: {self.student_name}"
    def get_id(self):
        return f"student id is: {self.student_id}"
    def get_course(self):
        return f"student course is: {self.course}"
    def get_status(self):
        return f"test status is: {self.test_status()}"

#creating student profile
s1=StudentProfile(1, "shyam", "python", 90)
 
print(s1.get_score())
print(s1.get_status())
print(s1.update_score(100))
print(s1.get_status())
    
