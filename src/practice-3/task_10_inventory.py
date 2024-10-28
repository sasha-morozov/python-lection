
things = {
    'key': 3,
    'mace': 1,
    'stone': 24,
    'lantern': 1,
    'gold coin': 10
}

print("Equipment:")
for item, count in things.items():
    print(f"{count} {item}")
print("Total number of things:", sum(things.values()))
