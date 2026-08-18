# public attribute
class StudentProfile:
    def __init__(self, name, id, score):
        self.student_name=name
        self.student_id=id
        self.student_score=score
    def test_status(self):
        if self.student_score>=40:
            print("Pass")
        else:
            print("Fail")
s1= StudentProfile("giri", 123, 39)
s1.test_status()

        
