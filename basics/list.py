pet_shop = ["dog", "cat", "rabbit", "snake", "hamster"]
zoo = ["lion", "tiger", "crocodile"]

print(pet_shop[0])
print(pet_shop[2:])

animal = pet_shop.copy()
animal.extend(zoo)

print(pet_shop)
print(animal)
