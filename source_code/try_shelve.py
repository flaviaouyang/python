import shelve
import os

print(os.getcwd())
os.chdir('/Users/flaviaouyang/AutomatePython/source_code')
print(os.getcwd())

# shelfFile = shelve.open('mydata')
# love = ['austyn', 'fitzgerald', 'water']
# shelfFile['love'] = love
# shelfFile.close()

# retrieveFile = shelve.open('mydata')
# print(retrieveFile['love'])
# retrieveFile['dog'] = ['dobie', 'golden']
# print(retrieveFile['dog'])
# retrieveFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

