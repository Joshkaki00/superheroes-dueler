import random
from ability import Ability
from armor import Armor

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
    self.abilities = []
    self.armors = []
    self.deaths = 0
    self.kills = 0

  def add_ability(self, ability):
    ''' Add ability to abilities list '''
    self.abilities.append(ability)

class Ability:
  def __init__(self, name, max_damage):
    '''
    Initialize the values passed into this
    method as instance variables.
    '''

    # Assign the "name" and "max_damage"
    # for a specific instance of the Ability class
    self.name = name
    self.max_damage = max_damage

  def attack(self):

    # Pick random value between 0 and the max_damage set
    random_value = random.randint(0, self.max_damage)
    return random_value

if __name__ == "__main__":
  hero1 = Hero("Wonder Woman", 150)
  hero2 = Hero("Dumbledore", 200)

  ability = Ability("Debugging Ability", 20)
  print(ability.name)
  print(ability.attack())

  # Start fight!
  hero1.fight(hero2)