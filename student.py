from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,title):
        self.modules.append(title)
        self.grades.update({title : title.get_grade()})

    def get_list_modules(self):
        print("Modules of Student {}".format(self.name))
        for object in self.modules:
            print("\t",object)

    def get_grades(self):
        print("Grades of Student {}".format(self.name))
        for key, value in self.grades.items():
            print("\t",key , ":" , value)



### test cases ###

me = Student("Maic Arpagaus")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
