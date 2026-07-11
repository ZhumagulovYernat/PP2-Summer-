import os
import shutil


source_folder = "test_folder"
target_folder = "test_folder/sub_folder"


file = "test_file.txt"


with open(file, "w") as f:
    f.write("Some text")


shutil.copy(file, source_folder)

print("File copied")


shutil.move(source_folder + "/" + file, target_folder)

print("File moved")


print(os.listdir(target_folder))