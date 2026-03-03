import os

# copy manually
with open("data.txt", "r") as f:
    content = f.read()

with open("backup.txt", "w") as f:
    f.write(content)

# delete backup
os.remove("backup.txt")