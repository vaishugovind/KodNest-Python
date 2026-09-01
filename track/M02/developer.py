class Developer:
    def work(self):
        print("Developer is working")
    
    def attendMeeting(self):
        print("Developer is attending the meeting")

class JavaDeveloper(Developer):
    def work(self):
        print("Java Developer is working")

    def DoJavaProject(self):
        print("Java developer is building a project")

class Pydeveloper(Developer):
    def work(self):
        print("Python Developer is working")
    def DoPyhtonProject(self):
        print("Python Developer is building a project")

dev=Developer()
dev.work()
dev.attendMeeting()
jdev=JavaDeveloper()
jdev.work()
jdev.attendMeeting()
jdev.DoJavaProject()
pdev=Pydeveloper()
pdev.work()
pdev.attendMeeting()
pdev.DoPyhtonProject()

    