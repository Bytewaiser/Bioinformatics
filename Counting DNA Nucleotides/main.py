from collections import Counter

with open ("data.txt", "r") as f:
    arr = f.read()

def return_counts(arr):
    counts = Counter(arr)
    return f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"
print(return_counts(arr))
