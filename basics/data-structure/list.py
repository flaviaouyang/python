pet_shop = ["dog", "cat", "rabbit", "snake", "hamster"]
zoo = ["lion", "tiger", "crocodile"]

print(pet_shop[0])

print(pet_shop[2:])
# inclusive

print(pet_shop[-1])

print(pet_shop[:2])
# exclusive

print(
    """
--------------------------------------------------------
      """
)

animal = pet_shop.copy()
animal.extend(zoo)

animal_list = ", ".join(animal)

print(pet_shop)
print(animal)
print(animal_list)

"""
output:

dog
['rabbit', 'snake', 'hamster']
hamster
['dog', 'cat']

--------------------------------------------------------

['dog', 'cat', 'rabbit', 'snake', 'hamster']
['dog', 'cat', 'rabbit', 'snake', 'hamster', 'lion', 'tiger', 'crocodile']
dog, cat, rabbit, snake, hamster, lion, tiger, crocodile
"""

to_be_sorted = [3, 10, 4, 2, 1, -4]
# to_be_sorted.sort()

sorted = sorted(to_be_sorted)
print(to_be_sorted)
print(sorted)
# output:
# [3, 10, 4, 2, 1, -4]
# [-4, 1, 2, 3, 4, 10]
