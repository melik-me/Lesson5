class Person:
    desc = "Hello"

    def __init__(self):
        self.fullname = ["Olena", "Piankova"]
        pass

    def set_name(self):
        self.name = "Olena"

    def set_something(self, x):
        self.something = x


p = Person()
p.set_name()

p.set_something("Ololo")

p2 = Person()
p2.set_something("Atata")
p2.set_name()

print(p.desc)
print(p.name)

print(p.something)
print(p2.something)

p.desc = '1'
print(p.desc)