import random
from hero import Hero

class Team:
    def __init__(self, name):
        ''' Initialize team with a name and an empty list of heroes.'''
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        ''' Add a hero to list of heroes.'''
        self.heroes.append(hero)

    def remove_hero(self, name):
        ''' Remove a hero from the team by name.
        If hero isn't found, return None.'''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return hero
        return 0

    def view_all_heroes(self):
        ''' Print the names of all heroes on the team.'''
        if not self.heroes:
            print("No heroes on this team.")
            return
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        ''' Print team statistics'''
        for hero in self.heroes:
            kd_ratio = hero.kills / hero.deaths if hero.deaths > 0 else hero.kills
            print(f"{hero.name} Kill/Deaths: {kd_ratio}")
