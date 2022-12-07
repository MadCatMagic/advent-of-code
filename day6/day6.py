
def fopen():
    with open("day6/day6-input.txt", "r") as f:
        data = f.read().strip()
        return data

def sequence(data, k):
    for i in range(k - 1, len(data)):
        d = {c: 0 for c in (data[i-k+1:i+1])}
        if len(d) == k:
            return i + 1
# part 1
data = fopen()
print(sequence(data, 4))

# part 2
print(sequence(data, 14))
