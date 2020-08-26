from datetime import date


class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def show_occupation(self):
        print(self.name + " is a Person with no job")

    def calculateAge(self):
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        print(self.name + "'s age is : " + str(age))


