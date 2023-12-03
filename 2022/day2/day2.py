def fopen():
    with open("day2/day2-input.txt", "r") as f:
        data = f.read().split("\n")
        return [(p[0], p[2]) for p in data]

def score(opponent, you):
    score = {"X": 1, "Y": 2, "Z": 3}[you]
    if {"X": 1, "Y": 2, "Z": 3}[you] == {"A": 1, "B": 2, "C": 3}[opponent]:
        score += 3
    else:
        for a, b in (("B", "Z"), ("C", "X"), ("A", "Y")):
            if opponent == a and you == b:
                score += 6
    return score

# part 1
data = fopen()
scores = [score(i, j) for i, j in data]
print(sum(scores))

# part 2
for i, (a, b) in enumerate(data):
    if b == "Y":
        data[i] = (a, {"A": "X", "B": "Y", "C": "Z"}[a])
    elif b == "X":
        data[i] = (a, {"A": "Z", "B": "X", "C": "Y"}[a])
    elif b == "Z":
        data[i] = (a, {"A": "Y", "B": "Z", "C": "X"}[a])

scores = [score(i, j) for i, j in data]
print(sum(scores))