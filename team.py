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
                foundHero = True
                break
        if not foundHero:
            return 0

    def view_all_heroes(self):
        ''' Print the names of all heroes on the team.'''
        if not self.heroes:
            print("No heroes on this team.")
            return
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

    # Add heroes to the team
    team.add_hero(hero1)
    team.add_hero(hero2)
    team.add_hero(hero3)

    # Print heroes
    print("Team members:")
    team.view_all_heroes()

    # Remove a hero and print updated team
    removed_hero = team.remove_hero("Iron Man")
    if removed_hero == 0:
        print(f"\nHero not found!")
    else:
        print(f"\nRemoved hero: {removed_hero}")

    print(f"\nUpdated team members:")
    team.view_all_heroes()