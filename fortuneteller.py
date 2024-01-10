import time


class FortuneTeller:
    def __init__(self, name, name_client=None, mood=False):
        self._name = name
        self._mood = mood
        self._name_client = name_client

    def fortune_telling(self):
        print(f"Сейчас я вам по гадаю секундочку...")
        self.timer()
        self.guess_name()

    def timer(self):
        print('Одеваю палатье')
        time.sleep(1)
        print('Одеваю туфли')
        time.sleep(1)
        print('Беру шар для гадания')
        time.sleep(1)
        print("Начнем !")

    def guess_name(self):
        print(f"Твое имя {self._name_client}")


