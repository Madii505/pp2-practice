with open("sample.txt", "w") as f:
    f.write("Line1\nLine2\nLine3\n")

with open("sample.txt", "r") as f:
    print("read():")
    print(f.read())

with open("sample.txt", "r") as f:
    print("readline():")
    print(f.readline())

with open("sample.txt", "r") as f:
    print("readlines():")
    print(f.readlines())