import os

os.makedirs("test_dir/sub_dir", exist_ok=True)

print("Current dir:", os.getcwd())
print("List:", os.listdir())

os.rmdir("test_dir/sub_dir")
os.rmdir("test_dir")