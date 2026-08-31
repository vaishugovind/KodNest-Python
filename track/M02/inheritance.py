class Parent():
   def __init__(self, name):
      self.name = name
      print("inside the parent constructor")

class Child(Parent):
   def __init__(self, name, course):
      self.__init__(name)     
      self.course = course
      print("inside the child constructor")

ch = Child("Rahul", "python")
print(ch.name)    
print(ch.course)   