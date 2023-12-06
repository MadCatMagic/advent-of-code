
def times(time, dist):
    s = 1
    for i, t in enumerate(time):
        k = 0
        for j in range(t + 1):
            if (t - j) * j > dist[i]:
                k += 1
        s *= k
    return s

with open("2023/day6input.txt", "r") as f:
    data = f.read().split("\n")
    arr = [[int(p) if i > 0 else p for i, p in enumerate(k.split())] for k in data]
    time = arr[0][1:]
    dist = arr[1][1:]
    s1 = times(time, dist)
    time, dist = [int(k[9:].replace(" ", "")) for k in data]
    s2 = times([time], [dist])
    print(s1, s2)
            