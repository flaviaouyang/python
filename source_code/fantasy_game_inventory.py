# You are creating a fantasy video game. The data structure to model the
# player’s inventory will be a dictionary where the keys are string values
# describing the item in the inventory and the value is an integer value detailing
# how many of that item the player has. For example, the dictionary value
# {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the
# player has 1 rope, 6 torches, 42 gold coins, and so on.
# Write a function named displayInventory() that would take any possible
# “inventory” and display it like the following:

# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62

inventory = {'arrow': 3,'gold coin': 5, 'rope': 64, 'torch': 99, 'dagger': 87}
def displayInventory(dict):
    print('Inventory:')
    total = 0
    for key, value in inventory.items():
        print(value, " ", key)
        total += value
    print("Total number of items: ", total)

# displayInventory(inventory)

# output:
# Inventory:
# 3   arrow
# 5   gold coin
# 64   rope
# 99   torch
# 87   dagger
# Total number of items:  258

# Imagine that a vanquished dragon’s loot is represented as a list of strings
# like this:
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# Write a function named addToInventory(inventory, addedItems), where the
# inventory parameter is a dictionary representing the player’s inventory (like
# in the previous project) and the addedItems parameter is a list like dragonLoot
# The addToInventory() function should return a dictionary that represents the
# updated inventory. Note that the addedItems list can contain multiples of the
# same item. 
# The previous program (with your displayInventory() function from the
# previous project) would output the following:
# Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger
# Total number of items: 48

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory (inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

addToInventory(inventory, dragonLoot)
displayInventory(inventory)