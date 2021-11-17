import sys
# print(True and True)
# print(True and False)
# print(True or False)
# print(False or False)
# print(True or True)

# name = input("Enter your name: ")
# if name == "Flavia":
#     print("Welcome, my magnificent master.")
# elif name == "Austyn":
#     print("Welcome, the beautiful companion of my magnificent master.")
# else:
#     print("ERROR!")

# counter = 0
# while counter < 5:
#     print ("You are wonderful")
#     counter += 1

# age = 20
# while age >= 18:
#     is_verified = input("Verification: ")
#     if is_verified == "verified":
#         print ("Have fun!")
#         break
#     else:
#         break

# while True:
#   code = input("What is the code word?\n")
#   if code != "cactus":
#   	continue
#   else:
#     print("Welcome")
#     break
# print("You're in.")

# for i in range (10):
#     print("Counting: " + str(i))

# grocery = ["banana", "brie", "basil", "pepper", "olive oil"]
# for item in grocery:
#     print("We are buying " + item)

# for i in range(12, 16):
#   print(i)
# # 12 13 14 15
# for i in range(0, 10, 2):
#   print(i)
# # 0 2 4 6 8
# for i in range (5, -1, -1):
#   print(i)
# # 5 4 3 2 1 0

while True:
    response = input("Enter \'exit\' to exit.\n")
    if response == "exit":
        sys.exit()
    print("Your response is " + response)
