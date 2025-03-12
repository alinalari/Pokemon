
from pokemon import Pokemon
import random

class DragonType(Pokemon):

    basic_attack = "Dragon Breath"
    prob = 0.3

    def __init__(self, name, trainer, hp = None):
        super().__init__(name, trainer)
        if hp is not None:
            self.hp = hp

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

            # Dragon attack gives damage to others
            # Dragon type is not strong or weak against anything
            #other.receive_damage(self.damage)
            super().attack(other)
            # Chance to paralyze opponent based on prob
            if random.random() < self.prob:
                other.paralyzed = True
                print(other.name, "is paralyzed!")
            # reset damage to original
            self.damage = Pokemon.damage
        else:
            print(f"{self.name} is paralyzed and can't attack.")
