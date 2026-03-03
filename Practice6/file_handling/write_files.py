# write
with open("data.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")

# append
with open("data.txt", "a") as f:
    f.write("New Line\n")

with open("data.txt", "r") as f:
    print(f.read())