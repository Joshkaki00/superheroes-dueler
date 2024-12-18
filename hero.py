import random
from ability import Ability
from armor import Armor
from weapon import Weapon

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

  def attack(self):
    ''' Calculate total damage from all abilities '''
    total_damage = sum(ability.attack() for ability in self.abilities)
    return total_damage

  def add_armor(self, armor):
    ''' Add armor to armors list '''
    self.armors.append(armor)

  def defend(self, damage_amount):
    total_block = sum(armor.block() for armor in self.armors)
    return max(0, damage_amount - total_block)  # Ensure block value is non-negative

  def take_damage(self, damage):
    '''Update current_health to reflect the damage minus the defense.'''
    damage_after_defense = self.defend(damage)
    self.current_health -= damage_after_defense
    if self.current_health < 0:
      self.current_health = 0

  def is_alive(self):
    '''Return True or False depending on whether the hero is alive or not.'''
    return self.current_health > 0

  def add_kill(self, num_kills):
    ''' Update kills with num_kills'''
    self.kills += num_kills

  def add_death(self, num_deaths):
    ''' Update deaths with num_deaths'''
    self.deaths += num_deaths

  def fight(self, opponent):
    '''Current Hero will take turns fighting the opponent hero passed in.'''
    # 0) Check if at least one hero has abilities
    if not self.abilities and not opponent.abilities:
      print("Draw! Neither hero has abilities.")
      return

    # 1) Start the fighting loop until a hero has won
    while self.is_alive() and opponent.is_alive():
      # Calculate damage dealt by each hero
      self_damage = self.attack()
      opponent_damage = opponent.attack()

      # Apply damage to each hero
      opponent.take_damage(self_damage)
      self.take_damage(opponent_damage)

      print(f"{self.name} attacks {opponent.name} for {self_damage} damage!")
      print(f"{opponent.name} attacks {self.name} for {opponent_damage} damage!")

      # 3) Check if either hero is alive
      if self.is_alive() and not opponent.is_alive():
        self.add_kill(1)
        opponent.add_death(1)
        print(f"{self.name} won!")
      elif not self.is_alive() and opponent.is_alive():
        opponent.add_kill(1)
        self.add_death(1)
        print(f"{opponent.name} won!")
      else:
        print("Both heroes have fallen!")
