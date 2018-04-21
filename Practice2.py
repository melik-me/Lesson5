# Создать метод класса Person, возвращающий полное имя.

class Person:
    def __init__(self, name='', surname='', age=-1):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self):
        """Возвращает имя с фамилией"""

        return self.name + " " + self.surname

    def get_older(self, years=1):
        """Увеличивает возраст на years лет, по умолчанию на 1"""

        self.age += years

    def __str__(self):
        """Переопределяем преобразование в строку"""
        return "<Person name={}, surname={}>".format(self.name, self.surname)

    # def __add__(self, person):
    #     """Переовпределяем сложене людей"""
    #     return Couple()

# class Couple:
#
#     def __init__(self):




if __name__ == "__main__":
    Vasya = Person("Vasya", "Pupkin", 18)
    print(Vasya.full_name())
    Vasya.get_older()
    print(Vasya.age)
    print(Vasya)
    print(str(Vasya))
    Petya = Person("Petya", "Sidorov", 20)
    VasyaPetya = Vasya + Petya
    print(VasyaPetya)