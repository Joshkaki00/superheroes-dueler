import random

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
        else:
            for hero in self.heroes:
                print(hero.name)

    def stats(self):
        ''' Print team statistics'''
        for hero in self.heroes:
            kd_ratio = hero.kills / hero.deaths if hero.deaths > 0 else hero.kills
            print(f"{hero.name} Kill/Deaths: {kd_ratio}")

    def revive_heroes(self):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other'''
        living_heroes = [hero for hero in self.heroes if hero and hero.is_alive()]
        living_opponents = [hero for hero in other_team.heroes if hero and hero.is_alive()]

        while living_heroes and living_opponents:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            print(f"{hero.name} battles {opponent.name}")
            hero.fight(opponent)

        if not living_heroes and not living_opponents:
            print("Both teams have been eliminated!")
        elif not living_heroes:
            print(f"Team {other_team.name} wins!")
        else:
            print(f"Team {self.name} wins!")
