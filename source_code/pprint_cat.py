import pprint
import os

os.chdir('/Users/flaviaouyang/AutomatePython/source_code')

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
cats_pp = pprint.pformat(cats)
file_obj = open('my_cats.py', 'w')
file_obj.write("cats= " + cats_pp + "\n")
file_obj.close()
