grocery = {}


def print_grocery(grocery):
    print("Grocery List: ")
    for k, v in grocery.items():
        print(v, " ", k)


def add_to_grocery(grocery, add_item):
    for item in add_item:
        grocery.setdefault(item, 0)
        grocery[item] += 1
    print_grocery(grocery)


today = ['apple', 'banana', 'brie', 'chips', 'beer', 'apple', 'apple']
add_to_grocery(grocery, today)
