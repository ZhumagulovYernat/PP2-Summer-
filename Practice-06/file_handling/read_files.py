file = "example.txt"


with open(file, "r", encoding="utf-8") as f:
    content = f.read()

print(content)


with open(file, "r", encoding="utf-8") as f:
    line = f.readline()

print(line)


with open(file, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(lines)