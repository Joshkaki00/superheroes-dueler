import random

class Armor:
  def __init__(self, name, max_block):
    '''Instantiate instance properties.
        name: String
        max_block: Integer
    '''
    self.name = name
    self.max_block = max_block


def block(self):
    return random.randint(0, self.max_block)