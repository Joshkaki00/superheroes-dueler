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
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return hero
        return None # Hero not found