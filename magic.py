import random

class Magic:
    """
    this Magic has name, mp cost, damage and type
    """
    def __init__(self, name, mp_cost, dmg, magic_type):
        self.name = name
        self.mp_cost = mp_cost
        self.dmg = dmg
        self.type = type
        self.high_dmg = dmg + 15
        self.low_dmg = dmg - 15
        self.magic_type = magic_type

    def generate_magic_dmg(self):
        dmg = random.randint(self.low_dmg, self.high_dmg)
        return dmg
