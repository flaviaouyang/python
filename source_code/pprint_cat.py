import pprint
import os
import my_cats

os.chdir('/Users/flaviaouyang/AutomatePython/source_code')

# cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# cats_pp = pprint.pformat(cats)
# file_obj = open('my_cats.py', 'w')
# file_obj.write("cats= " + cats_pp + "\n")
# file_obj.close()

print(my_cats.cats)
print(my_cats.cats[0])
print(my_cats.cats[1]['name'])


