from my_exceptions import *
from person import Person
from fortuneteller import FortuneTeller

name = str(input("what is your name: "))
age = int(input("How old are you: "))

people = Person(name, age)
# try:
#     people = Person(name, age)
#     if name == 'Глаша':
#         raise processingException('возникло исключение- ProcessingException')
# except ValueError as ex:
#     print(f'возникло исключение- ValueError {ex}')
# else:
#     f'Исключений не было'
# finally:
#     print('*' * 30)

try:
    witch = FortuneTeller('Глаша', name_client=people)
    if people is None:
        raise invalidDataException('возникло исключение- InvalidDataException')
except NameError as ex:
    print(f"Не получилось создать обьект человека и создать ведьму")
except ValueError as ex:
    print(f'возникло исключение- ValueError {ex}')
else:
    f'Исключений не было'

try:
    witch.fortune_telling()
except NameError as ex:
    print(f"Не получилось создать обьект и вызвать функцию по гадать")