import json


with open("sample-data.json", "r") as file:
    data = json.load(file)


print("Total count:", data["totalCount"])

print()

print("Interface Status")
print("=" * 90)
print(f"{'DN':50} {'Description':20} {'Speed':10} {'MTU':10}")
print("-" * 90)


for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]

    dn = attributes["dn"]
    description = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:50} {description:20} {speed:10} {mtu:10}")


new_data = {
    "name": "Practice 4",
    "topic": "JSON",
    "completed": True
}


json_string = json.dumps(new_data, indent=4)

print()
print(json_string)


with open("result.json", "w") as file:
    json.dump(new_data, file, indent=4)