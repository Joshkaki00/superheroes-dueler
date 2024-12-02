import random
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

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

  def defend(self, incoming_damage):
    if self.current_health <= 0:  # Dead heroes can't block
      return 0
    total_block = sum(armor.block() for armor in self.armors)
    return max(0, incoming_damage - total_block)  # Ensure block value is non-negative

  def take_damage(self, damage):
    '''Update current_health to reflect the damage minus the defense.'''
    damage_after_defense = self.defend(damage)
    self.current_health -= damage_after_defense
    if self.current_health < 0:
      self.current_health = 0

  def is_alive(self):
    '''Return True or False depending on whether the hero is alive or not.'''
    return self.current_health > 0

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
      if not opponent.is_alive() and not self.is_alive():
        print("Both heroes have fallen! It's a draw!")
        return
      elif not opponent.is_alive():
        print(f"{self.name} won!")
        self.kills += 1
        opponent.deaths += 1
        return
      elif not self.is_alive():
        print(f"{opponent.name} won!")
        opponent.kills += 1
        self.deaths += 1
        return


# Test code
if __name__ == "__main__":
  # Create abilities
  ability1 = Ability("Super Speed", 300)
  ability2 = Ability("Super Eyes", 130)
  ability3 = Ability("Wizard Wand", 80)
  ability4 = Ability("Wizard Beard", 20)

  # Create heroes
  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")

  # Add abilities to heroes
  hero1.add_ability(ability1)
  hero1.add_ability(ability2)
  hero2.add_ability(ability3)
  hero2.add_ability(ability4)

  # Add armor to heroes
  hero1.add_armor(Armor("Shield", 50))
  hero2.add_armor(Armor("Magic Robe", 40))

  # Engage in a fight
  hero1.fight(hero2)
