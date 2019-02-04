import random

class Person:
    def __init__(self, name, hp, mp, atk, magic):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk_high = atk + 10
        self.atk_low = atk - 10
        self.action = ["Physical Attack", "Magic"]
        self.magic = magic

    def stats(self):
        print(self.name)
        print(f"{self.hp}/{self.maxhp}")
        print(f"{self.mp}/{self.maxmp}")

    def generate_dmg(self): #through self input, init attributes can be accessed!!!
        """
            Generate the amount of damange randomly in range of highest attack and lowest Attack
        """
        dmg = random.randint(self.atk_low, self.atk_high) #import random, randint and randrange
        return dmg

    def take_dmg(self, dmg): #when enemy attacks, plaer takes/accepts damage.
        """
        When player takes damange, HP will be decreased
        """
        self.hp = self.hp - dmg
        if self.hp < 0 : #to avoid minus hp.
            self.hp = 0
        return self.hp

    def choose_action(self):
        index = 1
        print("ACTIONS: ")
        for element in self.action:
            print("{}. {}". format(index, element))
            index = index + 1

    def reduce_mp(self, used_mp):
        self.mp = self.mp - used_mp
        if self.mp < used_mp:
            print("Not enough Mana")
        return self.mp

    def choose_magic(self):
        index = 1
        print("Magic: ")
        for element in self.magic:
            print("{}. {}". format(index, element.name))
            index = index + 1
