class Person:

    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)

    def __str__(self):
        return f'Имя {self.name}, Возраст {self.age}'
