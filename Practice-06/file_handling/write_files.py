file = "example.txt"

with open(file, "w", encoding="utf-8") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")


with open(file, "a", encoding="utf-8") as f:
    f.write("New added line\n")


print("File was created and updated")