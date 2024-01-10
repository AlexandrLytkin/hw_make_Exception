from my_exceptions import *
from person import Person
from fortuneteller import FortuneTeller

name = str(input("what is your name: "))
age = int(input("How old are you: "))

try:
    people = Person(name, age)
    if name == 'Глаша':
        raise processingException('возникло исключение- ProcessingException')
except ValueError as ex:
    print(f'возникло исключение- ValueError {ex}')
finally:
    print('*' * 30)

try:
    witch = FortuneTeller('Глаша', name_client=people)
    if people is None:
        raise processingException('возникло исключение- InvalidDataException')
except ValueError as ex:
    if people is None:
        print(f'возникло исключение- ValueError {ex}')
    else:
        f'Исключений не было'

witch.fortune_telling()
