pet_shop = ["dog", "cat", "rabbit", "snake", "hamster"]
zoo = ["lion", "tiger", "crocodile"]

print(pet_shop[0])
print(pet_shop[2:])
print(pet_shop[-1])
print(pet_shop[:2])

print("""
--------------------------------------------------------
      """)

animal = pet_shop.copy()
animal.extend(zoo)

print(pet_shop)
print(animal)

# output:
# dog
# ['rabbit', 'snake', 'hamster']
# hamster
# ['dog', 'cat']

# --------------------------------------------------------
      
# ['dog', 'cat', 'rabbit', 'snake', 'hamster']
# ['dog', 'cat', 'rabbit', 'snake', 'hamster', 'lion', 'tiger', 'crocodile']
