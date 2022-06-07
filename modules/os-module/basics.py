import os

# print all methods
print(dir(os))

# get current directory and change directory
print(os.getcwd())
os.chdir("/Users/flaviaouyang/Python")
print(os.getcwd())
# output
# /Users/flaviaouyang/Python/os-module
# /Users/flaviaouyang/Python

print(os.listdir())

os.mkdir("mkdir-demo")
# will also make subdirectories
os.makedirs("mkdir-demo2/demo")

print(os.listdir())

os.rmdir("mkdir-demo")
os.removedirs("mkdir-demo2/demo")

print(os.listdir())
# output
# ['basics.py']
# ['mkdir-demo2', 'basics.py', 'mkdir-demo']
# ['basics.py']

os.mkdir("demo")
open("demo/demo.txt", "w").close()

os.rename("demo/demo.txt","demo/test.txt")

print(os.stat("demo/demo.txt"))
# output:
# os.stat_result(
#     st_mode=33188,
#     st_ino=70436661,
#     st_dev=16777221,
#     st_nlink=1,
#     st_uid=501,
#     st_gid=20,
#     st_size=0,
#     st_atime=1654561296,
#     st_mtime=1654561296,
#     st_ctime=1654561296,
# )

for dirpath, dirname, filename in os.walk(os.getcwd()):
  print(dirpath, dirname, filename)
# output
# /Users/flaviaouyang/Python/os-module ['demo'] ['basics.py']
# /Users/flaviaouyang/Python/os-module/demo [] ['demo.txt', 'test.txt']

# print(os.environ)
home = os.environ.get("HOME")
file_path = os.path.join(home, "test.txt")
print(file_path)
print(os.path.basename(file_path))
print(os.path.dirname(file_path))
print(os.path.exists(file_path))
print(os.path.isdir(file_path))
print(os.path.isfile(file_path))
print(os.path.splitext(file_path))
