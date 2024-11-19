# dog.py
class Dog:
  def __init__(self, name):
    self.name = name
    print("dog initialized!")

# the same instantiation call that creates a Dog object,
# but now we've assigned it to the value of the my_dog variable
my_dog = Dog("Rex")
print(my_dog)
print(my_dog.name)