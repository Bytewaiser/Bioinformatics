with open("data.txt", "r") as f:
    string = f.read()

print(string.replace("T", "U"))