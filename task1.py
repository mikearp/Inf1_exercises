class Module(object):

    ############################################################################

    def __init__(self,ects,title,semester,grade=None):
        "constructor for class module"

        # store everything as instance variables
        self.ects = ects
        self.grade = grade
        self.title = title
        self.semester = semester

        # create a list to store all important dates
        self.dates = []

        # create a list to store all module elements
        self.elements = []

    ############################################################################

    def get_important_dates_overview(self):
        "prints all the important dates for a module"

        print("Important dates for {0:s}:".format(self.title))

        for kind,date in self.dates:
            print("\t{0:s} on {1:s}".format(kind,date))

    ############################################################################

    def set_grade(self,grade):
        "set the grade to a given value"

        self.grade = grade

    ############################################################################

    def add_module_element(self,other_class,date):
        "add a new module element to the elements list"

        obj = other_class(self)
        obj.add_important_date(date)
        self.elements.append((obj))

################################################################################

class ModuleElement(object):

    ############################################################################

    def __init__(self,module):
        "constructor for class module element"

        # store module as instance variable
        self.module = module

    ############################################################################

    def add_important_date(self,kind,date):
        "add a date to the module's date dictionary"

        self.module.dates.append((kind,date))


################################################################################

class Lesson(ModuleElement):

    ############################################################################

    def __init__(self,module):
        "constructor for class lesson"

        # call super class constructor
        ModuleElement.__init__(self,module)

    ############################################################################

    def add_important_date(self,date):
        "add a lesson to the date dictionary"

        ModuleElement.add_important_date(self,"Lesson",date)

################################################################################

class Lab(ModuleElement):

    ############################################################################

    def __init__(self,module):
        "constructor for class lab"

        # call super class constructor
        ModuleElement.__init__(self,module)

    ############################################################################

    def add_important_date(self,date):
        "add a lab session to the date dictionary"

        ModuleElement.add_important_date(self,"Lab Session",date)

################################################################################

class Midterm(ModuleElement):

    ############################################################################

    def __init__(self,module):
        "constructor for class midterm"

        # call super class constructor
        ModuleElement.__init__(self,module)

    ############################################################################

    def add_important_date(self,date):
        "add a midterm to the date dictionary"

        ModuleElement.add_important_date(self,"Midterm",date)

################################################################################

class FinalExam(ModuleElement):

    ############################################################################

    def __init__(self,module):
        "constructor for class final exam"

        # call super class constructor
        ModuleElement.__init__(self,module)

    ############################################################################

    def add_important_date(self,date):
        "add a final exam to the date dictionary"

        ModuleElement.add_important_date(self,"Final Exam",date)

################################################################################


### test cases ###

# info1 = Module(6,"Info 1",1)
# info1.add_module_element(Midterm,"31.10.2017")
# info1.add_module_element(FinalExam,"20.12.2017")
# info1.get_important_dates_overview()
