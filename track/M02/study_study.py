class Student:
    def study(self):
        print(self.name, "is studying")

s1 = Student()
s1.roll_no = 11
s1.name = "Amit"
s1.age = 21
s1.marks = 85


s2 = Student()
s2.roll_no = 12
s2.name = "Arun"
s2.age = 22
s2.marks = 90

s1.study()
print(s1.roll_no)
print(s1.name)
print(s1.age)
print(s1.marks)

s2.study()
print(s2.roll_no)
print(s2.name)
print(s2.age)
print(s2.marks)