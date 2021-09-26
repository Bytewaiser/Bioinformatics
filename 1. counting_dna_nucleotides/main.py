from collections import Counter

with open ("data.txt", "r") as f:
    string = f.read()

def return_counts(string):
    counts = Counter(string)
    return f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"
print(return_counts(string))
