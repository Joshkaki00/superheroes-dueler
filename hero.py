import random

# hero.py
class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, starting_health=100):
    '''Instance properties:
      name: String
      starting_health: Integer
      current_health: Integer
    '''
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

    def fight(self, opponent):
      ''' Current Hero will take turns fighting the opponent hero passed in.
      '''
      # Randomly declare winner
      winner = random.choice([self, opponent])
      # Print name of the winner
      print(f"{winner.name} won!")

if __name__ == "__main__":
  hero1 = Hero("Wonder Woman", 150)
  hero2 = Hero("Dumbledore", 200)

  # Start fight!
  hero1.fight(hero2)