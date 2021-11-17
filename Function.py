import random
# this function that takes a string as an input
# and output the number of characters
# def num_of_string(word):
#     return len(word)

# print(num_of_string("Hello"))
# print(num_of_string("Hi"))
# print(num_of_string("superbondalicious"))

# print("Hello", end="")
# print("World")

# print("cats", "dogs", "mice", sep="-")

# def division(denominator):
#     try:
#         return 100/denominator
#     except ZeroDivisionError:
#         print ("Error: Invalid argument.")

# # print(division(10))
# print(division(0))


# a short program: guess the number
# show the user if their guess is correct
answer = random.randint(1, 100)
while True:
    guess = int(input("Your guess: "))
    if guess == answer:
        print("Correct. The answer is " + str(answer))
        break
    elif guess > answer:
        print("Too big.")
        continue
    else:
        print("Too small")
        continue