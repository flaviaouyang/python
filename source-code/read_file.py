import os

# print(os.path.join('Users', 'flaviaouyang', 'AutomatePython', 'source_code'))
# print(os.getcwd())
# os.chdir('/Users/flaviaouyang')
# print(os.getcwd())
# os.makedirs('test123')
# print(os.path.isabs('.'))
# print(os.path.isabs(os.path.abspath('.')))
# print(os.path.dirname(os.getcwd()))
# print(os.path.basename(os.getcwd()))
# print(os.path.split(os.getcwd()))
# print(os.path.getsize(os.getcwd()))
# print(os.listdir(os.getcwd()))
# print(os.path.isdir('.'))

test_file = open('/Users/flaviaouyang/AutomatePython/notes/Test.txt')
test_content = test_file.read()
print(test_content, '\n\n')
gluck_file = open('/Users/flaviaouyang/AutomatePython/notes/gluck.txt')
gluck_content = gluck_file.readlines()
# print(gluck_content)

test_file.close()
gluck_file.close()

test_file = open('/Users/flaviaouyang/AutomatePython/notes/Test.txt', 'w')
test_file.write("I love my girlfriend so damn much.")
test_file.close()

gluck_file = open('/Users/flaviaouyang/AutomatePython/notes/gluck.txt', 'a')
gluck_file.write("Awesome")
gluck_file.close()
