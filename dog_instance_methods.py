class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instances Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # Instance Method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

mikey = Dog("Mikey", 9)

print(mikey.description())
print(mikey.speak("Gruff Gruff"))
