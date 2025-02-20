import json
with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 50)
print("{:<50} {:<10} {:<10}".format("DN", "Speed", "MTU"))
print("-" * 50)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print("{:<50} {:<10} {:<10}".format(dn, speed, mtu))

