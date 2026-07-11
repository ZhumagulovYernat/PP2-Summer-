import os
from pathlib import Path


folder = "test_folder/sub_folder"


os.makedirs(folder, exist_ok=True)


print(os.getcwd())


files = os.listdir(".")

print(files)


path = Path(".")

for file in path.iterdir():
    if file.suffix == ".py":
        print(file)