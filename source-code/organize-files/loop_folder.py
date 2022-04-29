import os

for folder_name, subfolders, filenames in os.walk(os.getcwd()):
    print("Folder name is", folder_name)
    
    for subfolder in subfolders:
        print("Subfolder of",folder_name, "is", subfolder)
        
    for filename in filenames:
        print("Inside", folder_name, "is", filename)
        

# output:
# Folder name is /Users/flaviaouyang/Automate-Python/source-code/organize-files
# Subfolder of /Users/flaviaouyang/Automate-Python/source-code/organize-files is to-be-copied
# Subfolder of /Users/flaviaouyang/Automate-Python/source-code/organize-files is copy-to-here
# Inside /Users/flaviaouyang/Automate-Python/source-code/organize-files is walk-through-directory.py
# Inside /Users/flaviaouyang/Automate-Python/source-code/organize-files is organize.py
# Folder name is /Users/flaviaouyang/Automate-Python/source-code/organize-files/to-be-copied
# Inside /Users/flaviaouyang/Automate-Python/source-code/organize-files/to-be-copied is romeo.txt
# Folder name is /Users/flaviaouyang/Automate-Python/source-code/organize-files/copy-to-here
# Inside /Users/flaviaouyang/Automate-Python/source-code/organize-files/copy-to-here is romeo.txt