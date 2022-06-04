print("Imported my_mod")

passcode = 1234

def find_index(to_search, target):
  for index, value in enumerate(to_search):
    if value == target:
      return index
  return "Not found"