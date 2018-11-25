class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instances Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
william = Dog("William", 7)

def get_biggest_number(*args):
    return max(args)

print("The oldest dog is {} years old.".format(get_biggest_number(philo.age, mikey.age, william.age)))
