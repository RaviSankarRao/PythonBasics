class Student:

    # class initialize function
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def display_student(self):
        return self.name + " : Major :  " + self.major + " : GPA : " + str(self.gpa) + " : Is on probation : " + str(self.is_on_probation)