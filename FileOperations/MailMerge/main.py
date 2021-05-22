names = []
content = ""
with open("template.txt") as file:
    content = file.read()

with open("names/name.txt") as file:
    names = file.readlines()

names = [x.strip() for x in names]

for name in names:
    data = content.replace('NAME', name)
    with open(f"letters/{name}.txt", 'w') as file:
        file.write(data)
