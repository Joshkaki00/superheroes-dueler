from ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        '''Return a random value between half and the full attack power.'''
        return random.randint(self.max_damage // 2, self.max_damage)
