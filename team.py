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

    def view_all_heroes(self):
        ''' Print the names of all heroes on the team.'''
        for hero in self.heroes:
            print(hero.name)

# Test Team class
if __name__ == "__main__":
    # Create heroes
    hero1 = Hero("Wonder Woman", 200)
    hero2 = Hero("Iron Man", 150)
    hero3 = Hero("Deadpool", 180)

# Create team
team = Team("Justice League")