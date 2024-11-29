import random

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
    random_value = random.randint(0, self.max_damage)
    return random_value

# Test the Ability class

if __name__ == "__main__":
  ability = Ability("Super Punch", 50)

# Print the ability name
print(ability.name)

# Test attack method
print(ability.attack())