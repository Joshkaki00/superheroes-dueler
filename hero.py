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

  def attack(self):
    ''' Calculate total damage from all abilities '''
    total_damage = sum([ability.attack() for ability in self.abilities])
    return total_damage

  def add_armor(self, armor):
    ''' Add armor to armors list '''
    self.armors.append(armor)

  def defend(self, incoming_damage):
    ''' Calculate total block amount from all armors '''
    total_block = sum([armor.block() for armor in self.armors])
    damage_blocked = max(0, incoming_damage - total_block)
    return damage_blocked

  def take_damage(self, damage):
    ''' Update current_health with damage '''
    damage_after_block = self.defend(damage)
    self.current_health -= damage_after_block
    if self.current_health <= 0:
      self.current_health = 0
      self.deaths += 1

  def is_alive(self):
    ''' Return True or False depending on whether the hero is alive or not '''
    return self.current_health > 0

  def fight(self, opponent):
    ''' Engage in a battle with another hero '''
    while self.is_alive() and opponent.is_alive():
      self_damage = self.attack()
      opponent_damage = opponent.attack()

      opponent.take_damage(self_damage)
      self.take_damage(opponent_damage)

      print(f"{self.name} attacks {opponent.name} for {self_damage} damage!")
      print(f"{opponent.name} attacks {self.name} for {opponent_damage} damage!")

    if self.is_alive():
      self.kills += 1
      opponent.deaths += 1
    elif opponent.is_alive():
      opponent.kills += 1
      self.deaths += 1
    else:
      print("Both heroes have fallen!")

# Test hero class
if __name__ == "__main__":
  # Create abilities
  super_punch = Ability("Super Punch", 50)
  heavy_attack = Ability("Heavy Attack", 85)
  shield_bash = Ability("Shield Bash", 35)

  # Create armor
  shield = Armor("Steel Shield", 50)
  chestplate = Armor("Bronze Chestplate", 25)

  # Create hero
  hero1 = Hero("Elise", 200)
  hero2 = Hero("Lanavaille", 200)

  # Add abilities and armor to hero1
  hero1.add_ability(super_punch)
  hero1.add_ability(heavy_attack)
  hero1.add_armor(shield)
  hero1.add_armor(chestplate)

  # Add abilities and armor to hero2
  hero2.add_ability(shield_bash)
  hero2.add_ability(Armor("Iron Helmet", 30))

  # Start fight
  hero1.fight(hero2)
