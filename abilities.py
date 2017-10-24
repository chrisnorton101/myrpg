import random


class Ability:
    def __init__(self, name, dmg, cost, desc):
        self.name = name
        self.dmg = dmg
        self.cost = cost
        self.desc = desc

    def generate_dmg(self):
        low = self.dmg - 5
        high = self.dmg + 5
        return random.randrange(low, high)
