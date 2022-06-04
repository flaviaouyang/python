herbivore = {"cow", "horse", "sheep", "rabbit"}
omnivore = {"puma", "crocodile", "lion", "tiger"}
animal = herbivore.union(omnivore)

print(herbivore.intersection(omnivore))
print(herbivore.difference(omnivore))
print(herbivore ^ omnivore)
print(animal)

# add and update
herbivore.add("buffalo")
omnivore.update(["wolf", "panther"])
print(herbivore)
print(omnivore)

# note
# creating an empty set

false_set = {}
print(type(false_set))
# this will create an empty dictionary

empty_set = set()
print(type(empty_set))
# this will create an empty set

# output:
# <class 'dict'>
# <class 'set'>