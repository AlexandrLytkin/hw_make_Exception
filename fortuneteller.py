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
        time.sleep(1.5)
        print('Одеваю палатье')
        time.sleep(1.5)
        print('Одеваю туфли')
        time.sleep(1.5)
        print('Беру шар для гадания')
        time.sleep(2)
        print("Начнем !")

    def guess_name(self):
        print(f"Ты являешся {self._name_client}")
