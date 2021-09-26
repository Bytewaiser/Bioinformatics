def reverse_complement(string):
    string = string[::-1]
    d = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(list(map(lambda x: d[x],string)))

with open("data.txt", "r") as f:
    string = f.read()[:-1]

print(reverse_complement(string))