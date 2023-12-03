
def fopen():
    with open("day14/day14-input.txt", "r") as f:
        data = f.read().strip().split("\n")
        grid = [[0 for y in range(200)] for x in range(1000)]
        ground = 0
        for line in data:
            line = [[int(bit) for bit in sect.split(",")] for sect in line.split("->")]
            for pair in line:
                ground = max(ground, pair[1])
            for i in range(len(line) - 1):
                # find dir
                dir = (line[i + 1][0] - line[i][0], line[i + 1][1] - line[i][1])
                # find diff
                diff = abs(dir[0]) + abs(dir[1])
                dir = (0 if dir[0] == 0 else dir[0] // abs(dir[0]), 0 if dir[1] == 0 else dir[1] // abs(dir[1]))
                # fill in grid
                for j in range(diff + 1):
                    grid[line[i][0] + dir[0] * j][line[i][1] + dir[1] * j] = 1
        ground += 2
        return grid, ground

# part 1
def run(grid):
    start = (500, 0)
    i = 0
    while True:
        pos = start
        if grid[pos[0]][pos[1]] != 0:
            return i
        while True:
            if pos[1] == 199:
                return i
            if grid[pos[0]][pos[1] + 1] == 0:
                pos = (pos[0], pos[1] + 1)
            else:
                if grid[pos[0] - 1][pos[1] + 1] == 0:
                    pos = (pos[0] - 1, pos[1] + 1)
                elif grid[pos[0] + 1][pos[1] + 1] == 0:
                    pos = (pos[0] + 1, pos[1] + 1)
                else:
                    grid[pos[0]][pos[1]] = 2
                    break
        i += 1

grid, ground = fopen()
print(run(grid))

# part 2
grid, ground = fopen()
for i in range(1000):
    grid[i][ground] = 1
print(run(grid))

# import matplotlib.pyplot as plt
# 
# fig, ax = plt.subplots()
# ax.imshow(grid)
# 
# plt.grid(which="both",axis="both")
# plt.show()