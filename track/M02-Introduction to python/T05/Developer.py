class Developer:
    def working(self):
        print("Developer is working")
    def attendmeeting(self):
        print("Developer is attending meeting")

class JavaDeveloper(Developer):
    def work(self):
        print("JavaDeveloper is working")
    def doJavaProject(self):
        print("JavaDeveloper is doing java projects")

class PythonDeveloper(Developer):
    def work(self):
        print("PythonDeveloper is working")
    def doPythonProjects(self):
        print("PythonDeveloper is doing python projects")


javaDev = JavaDeveloper()
javaDev.work()
javaDev.doJavaProject()
javaDev.attendmeeting()

pythonDev = PythonDeveloper()
pythonDev.work()
pythonDev.doPythonProjects()
pythonDev.attendmeeting()



  