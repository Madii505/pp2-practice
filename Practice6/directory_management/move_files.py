import shutil
import os

os.mkdir("folder1")
os.mkdir("folder2")

with open("folder1/example.txt", "w") as f:
    f.write("Move me")

shutil.move("folder1/example.txt", "folder2/example.txt")