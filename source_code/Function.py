import random
# this function that takes a string as an input
# and output the number of characters
def num_of_string(word):
    return len(word)

print(num_of_string("Hello"))
print(num_of_string("Hi"))
print(num_of_string("superbondalicious"))

print("Hello", end="")
print("World")

print("cats", "dogs", "mice", sep="-")

def division(denominator):
    try:
        return 100/denominator
    except ZeroDivisionError:
        print ("Error: Invalid argument.")

# print(division(10))
print(division(0))


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


# The Collatz Sequence
# Write a function named collatz() that has one parameter named number. If
# number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.
# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1.
# (Amazingly enough, this sequence actually works for any integer—sooner
# or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t
# sure why. Your program is exploring what’s called the Collatz sequence, sometimes
# called “the simplest impossible math problem.”)
# Remember to convert the return value from input() to an integer with
# the int() function; otherwise, it will be a string value.

def collatz(number):
    if number % 2 == 0:
        print (number // 2)
        return number // 2
    elif number % 2 == 1:
        print (3 * number + 1)
        return 3 * number + 1

try:
    num = int(input("Enter a number: \n"))
except ValueError:
    print("Error: input is not an integer.")

while True:
    check = collatz(num)
    if check == 1:
        break
    else:
        num = check
        continue