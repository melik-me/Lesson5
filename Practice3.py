from Practice2 import Person

class Employee(Person):
    pass

    def __init__(self, name='', surname='', age=-1, position=None, salary=0):
        Person.__init__(self, name, surname, age)
        self.position = position
        self.salary = salary

    def __str__(self):
        return "<Employee name={}, surname={}>".format(self.name, self.surname)

    def income(self, months):
        return self.salary*months


if __name__ == "__main__":
    e = Employee(age=10, salary=100)
    print(e)
    e.get_older(10)
    print(e.age)
    print(Employee.income(e, 4))