file = open("data.txt")
content = file.read()
print(content)
file.close()

with open("data.txt") as file:
    content = file.read()
    print("In With block\n\t"+content)

with open("data.txt", "a") as file:
    file.write("\nDummy text.")
