import my_mod as mm
from my_mod import find_index

courses = ["philosophy", "pythons", "calculus"]

index = find_index(courses, "rabbit")
print(index)

index = mm.find_index(courses, "calculus")
print(index)

print(mm.passcode)