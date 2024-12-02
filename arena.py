from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        ''' Instantiate properties
            team_one: None
            team_two: None'''
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")
    def create_ability(self):
        ''' Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What is the ability name? ")
        max_damage = int(input("What is the max damage of the ability? "))
        return Ability(name, max_damage)

    def create_weapon(self):
        ''' Prompt user for Weapon info
            return Weapon with values from user input'''
        name = input("What is the weapon name? ")
        max_block = int(input("What is the max block of the armor? "))
        return Armor(name, max_block)

    def create_hero(self):
        ''' Prompt user for Hero info
            return Hero with values from user input'''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input(f"[1] Add ability\n [2] Add weapons\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_ability(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero