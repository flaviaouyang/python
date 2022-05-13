# object
class Dog:
    # attributes
    
    # private double underscore
    # The private members of a class are only accessible within the class.
    
    # protected single underscore
    # protected members of a class can be accessed by other members within the class and are also available to their subclasses.
    __dogs = []

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__dogs.append(self)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def __add__(self, other):
        return Dog("Hybrid DOG", self.age + other.age)

    def __sub__(self, other):
        return Dog("Hybrid DOG", self.age - other.age)

    def __str__(self):
        return f"A dog named {self.name} and age {self.age}"

    # greater than
    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    # greater or equal to
    def __ge__(self, other):
        return self.age >= other.age

    def __eq__(self, other):
        return self.age == other.age

    # not referencing specific instances
    # but in reference to the class
    @classmethod
    def num_dogs(cls):
        return len(cls.__dogs)

    @classmethod
    def get_all_dogs(cls):
        output = ""
        for i in cls.__dogs:
            output += str(i)
        return output

    # cannot access self or cls in static methods
    # use them only as a function
    # cannot change state of class hence static
    @staticmethod
    def make_sounds(cls):
        print("Raff...")

# inheritance
# object Cat inherits from Dog
class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        print(color)

    def make_sounds(self):
        print("Meow...")


archie = Dog("Archie", 10)
ollie = Dog("Ollie", 1)

print(Dog.num_dogs())
print(Dog.get_all_dogs())
for dog in Dog._Dog__dogs:
    print(dog)
    
# print(Dog._Dog__dogs)
