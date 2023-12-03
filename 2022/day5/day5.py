
# want to arrange into stacks/instructions
def fopen():
    with open("day5/day5-input.txt", "r") as f:
        data = f.read().split("#seperator")

        stackData = data[0].strip().split("\n")
        stackData.reverse()
        stackCount = int(stackData[0].split(" ")[-1])
        stackData.pop(0)
        stacks = [[] for _ in range(stackCount)]
        # iterate through and append to stacks in order
        for i, line in enumerate(stackData):
            for i in range(stackCount):
                if line[i * 4 + 1] != " ":
                    stacks[i].append(line[i * 4 + 1])

        # converts into stack indices
        instructions = [(int(i[1]), int(i[3]) - 1, int(i[5]) - 1) for i in [l.split(" ") for l in data[1].strip().split("\n")]]
        return stacks, instructions

# part 1
stacks, instructions = fopen()
for i in instructions:
    for _ in range(i[0]):
        stacks[i[2]].append(stacks[i[1]][-1])
        stacks[i[1]].pop()
print("".join([s[-1] for s in stacks]))

# part 2
stacks, instructions = fopen()
for i in instructions:
    for j in range(i[0]):
        stacks[i[2]].append(stacks[i[1]][-i[0] + j])
    for _ in range(i[0]):
        stacks[i[1]].pop()
print("".join([s[-1] for s in stacks]))