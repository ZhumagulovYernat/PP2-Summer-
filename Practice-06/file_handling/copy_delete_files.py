import shutil
import os


source = "example.txt"
copy_file = "example_copy.txt"


shutil.copy(source, copy_file)

print("File copied")


if os.path.exists(copy_file):
    os.remove(copy_file)
    print("File deleted")
else:
    print("File not found")