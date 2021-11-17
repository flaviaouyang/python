import copy
# roster = [['Gloria', 'Manny', 'Joe', 'Jay', 'Stella'],['Phil', 'Claire', 'Alex', 'Luke', 'Haley'], ['Lily', 'Mitchell', 'Cam', 'Larry']]
# print(roster[1][1])

# rating = [9, 8, 10, 10, 7, 9]
# redacted_rating = rating[1:4]
# # print(rating)
# print(redacted_rating)
# redacted_rating = rating[2:]
# print(redacted_rating)
# redacted_rating = rating[:5]
# print(redacted_rating)

# print(len(rating))

# grade = [100, 95, 90, 100]
# grade_dup = grade * 3
# # print(grade_dup)
# grade.pop()
# print(grade)
# del grade[1]
# print(grade)
# del grade
# print(grade)

# austyn = []
# while True:
#     adj = input("Describe Austyn: ")
#     if adj == '':
#         break
#     austyn += [adj]

# print("Austyn is ", end="")
# for i in austyn:
#     print(i, end=", ")
# print("and wonderful.\n")

# if "ugly" not in austyn:
#     print("Austyn is not ugly.")
# else:
#     print("Austyn is ugly.")

dog = ['doberman', 'golden', 'corgi']
# print(dog)
# dog.append('german sheperd')
# print(dog)
# dog.insert(1, 'chihuahua')
# print(dog)
# dog.remove('corgi')
# print(dog)

# dog.sort()
# print(dog)
# dog.sort(reverse=True)
# print(dog)

# dog_tuple = tuple(dog)
# print(dog_tuple)

dog_1 = dog
dog_2 = copy.copy(dog)

dog_1[1] = 20

print (dog)
print (dog_1)
print(dog_2)