from Person import Person


class Employee(Person):

    # function override - The same function exists in Person as well
    def show_occupation(self):
        print(self.name + " is an Employee and has a job")