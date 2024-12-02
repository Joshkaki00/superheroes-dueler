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
        max_damage = int(input("What is the max damage of the weapon? "))
        return Weapon(name, max_damage)

    def create_armor(self):
        ''' Prompt user for Armor info
            return Armor with values from user input'''
        name = input("What is the armor name? ")
        while True:
            try:
                max_block = int(input("What is the max block of the armor? "))
                break
            except ValueError:
                print("Please enter a valid number.")
        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero info and return a Hero object'''
        while True:
            hero_name = input("Hero's name: ").strip()
            if not hero_name:
                print("Hero name cannot be empty. Please try again.")
                continue  # Retry until valid input is provided

            hero = Hero(hero_name)
            while True:
                add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
                if add_item == "1":
                    ability = self.create_ability()
                    hero.add_ability(ability)
                elif add_item == "2":
                    weapon = self.create_weapon()
                    hero.add_ability(weapon)
                elif add_item == "3":
                    armor = self.create_armor()
                    hero.add_armor(armor)
                elif add_item == "4":
                    break  # Exit the loop when done adding items
                else:
                    print("Invalid choice. Please select a valid option.")
            return hero

    def build_team_one(self):
        '''Prompt the user to build team_one'''
        num_of_heroes = int(input("How many members would you like on Team One? "))
        for _ in range(num_of_heroes):
            hero = self.create_hero()
            if hero:  # Only add non-None hero objects
                self.team_one.add_hero(hero)

def build_team_two(self):
    '''Prompt the user to build team_two'''
    num_of_heroes = int(input("How many members would you like on Team Two? "))
    for _ in range(num_of_heroes):
        hero = self.create_hero()
        if hero:  # Only add non-None hero objects
            self.team_two.add_hero(hero)

    def team_battle(self):
        ''' Battle teams against each other '''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        ''' Show the team's stats '''
        print(f"\nTeam One statistics: ")
        self.team_one.stats()
        print(f"\nTeam Two statistics: ")
        self.team_two.stats()

        # Calculate Team One's average K/D
        team_one_kills = sum(hero.kills for hero in self.team_one.heroes)
        team_one_deaths = sum(hero.deaths for hero in self.team_one.heroes)
        if team_one_deaths == 0:
            team_one_deaths = 1
        print(f"Team One average K/D: {team_one_kills/team_one_deaths:.2f}")

        # Calculate Team Two's average K/D
        team_two_kills = sum(hero.kills for hero in self.team_two.heroes)
        team_two_deaths = sum(hero.deaths for hero in self.team_two.heroes)
        if team_two_deaths == 0:
            team_two_deaths = 1
        print(f"Team Two average K/D: {team_two_kills/team_two_deaths:.2f}")

        # Show surviving heroes
        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(f"Survivor from Team One: {hero.name}")
        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(f"Survivor from Team Two: {hero.name}")

# Game Loop
if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        # Battle teams
        arena.team_battle()

        # Show results of the battle
        arena.show_stats()

        play_again = input("Play Again? Y or N: ")
        if play_again.lower() == "n":
            game_is_running = False
        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()