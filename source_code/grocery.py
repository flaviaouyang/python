grocery = {}


def display_grocery(grocery):
    print("Grocery List: ")
    for k, v in grocery.items():
        print(v, " ", k)
    total = 0
    for v in grocery.values():
        total += v
    print("Total items:", total)


def add_to_grocery(grocery, added_item):
    for item in added_item:
        grocery.setdefault(item, 0)
        grocery[item] += 1
    display_grocery(grocery)


to_buy = []
num = int(input('How many items would you like to add to grocery list: '))
for i in range(num):
    item = input("To buy: ")
    to_buy.append(item)

add_to_grocery(grocery, to_buy)
