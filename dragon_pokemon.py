
from pokemon import Pokemon
import random

class DragonType(Pokemon):

    def __init__(self, name, trainer, hp = None):
        super().__init__(name, trainer)
        if hp is not None:
            self.hp = hp
        self.basic_attack = "Dragon Breath"
        self.prob = 0.3

    def __str__(self):
        return (f" Pokemon name: {self.name} (Dragon Type)\t "
                f" Trainer: {self.trainer}\t "
                f" Level: {self.level}, "
                f" HP: {self.hp},"
                f" Paralyzed: {self.paralyzed}")

    def attack(self, other):
        if not self.paralyzed:
            self.speak()
            print(f"{self.name} used {self.basic_attack}!")

            # Dragon type is not strong or weak against anything
            self.damage = Pokemon.damage
            # Dragon attacks others
            super().attack(other)
            # Chance to paralyze others based on prob
            if (random.random() < self.prob and
                    type(other) != DragonType):
                other.paralyzed = True
                print(other.name, "is paralyzed!")
            # reset damage to original
            self.damage = Pokemon.damage
        else:
            print(f"{self.name} is paralyzed and can't attack.")
