# WJ_Splishy Splash_pokemon.py by Weihua Jiang

import random

class Pokemon:
    basic_attack = 'tackle'
    damage = 40;

    def __init__(self, name, trainer):
        self.name = name
        self.trainer = trainer
        self.level = 1
        self.hp = 50
        self.paralyzed = False

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        if not self.paralyzed:
            self.speak()
            print(self.name, ' used ', self.basic_attack, '!')
            other.receive_damage(self.damage)

    def receive_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            print(self.name, ' fainted!')

class WaterType(Pokemon):

    def __init__(self, watertype_name, water_type_trainer, hp = None):
        super().__init__(watertype_name, water_type_trainer)
        if hp != None:
            self.hp = hp
        self.prob = 0.3
        self.basic_attack = "Splishy Splash"

    def __str__(self):
        ret_str = "Pokemon name: {}\t Trainer: {}\n"\
                  "Level: {}\tHP: {}\n"\
                  "Basic_Attack: {}\t Probility to Paralyze: {}".format(self.name, self.trainer, self.level, self.hp, self.basic_attack, self.prob)
        return ret_str

    def __repr__(self):
        ret_str = "WaterType({})".format(self.name)
        return ret_str

    def attack(self, other):
        #not weerk or strong against any pokemons
        self.damage = Pokemon.damage
        # run attack
        super().attack(other)
        # check to see if pokemon paralyzed
        if random.random() < self.prob and type(other) != WaterType:
            other.paralyzed = True
            print(other.name, "is paralyzed!")
        # reset damage to original
        self.damage = Pokemon.damage

