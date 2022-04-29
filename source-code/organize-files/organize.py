import send2trash

# get current files
# print(os.getcwd())

# copies romeo from to-be-copied directory to copy-to-here directory
# shutil.copy("to-be-copied/romeo.txt", "copy-to-here")

# safe delete
nonsense_file = open("nonsense.txt", "a")
nonsense_file.write("Pariatur aliqua id nulla eu non laborum excepteur pariatur excepteur amet.")
nonsense_file.close()
send2trash.send2trash("nonsense.txt")