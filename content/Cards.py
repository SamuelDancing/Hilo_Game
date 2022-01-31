import random

class cards:
    def __init__(self):
        self.card = 0

    def new_card(self):
        self.card = random.randint(1, 13)