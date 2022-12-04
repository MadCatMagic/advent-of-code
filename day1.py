f = open("day1-input.txt", "r")
data = f.read()
f.close()

ints = [[int(n) for n in bloc.split("\n")] for bloc in data.split("\n\n")]
sums = [sum(elf) for elf in ints]

# part 1
print(max(sums))

# part 2
# inefficent but it works
# im not using daniel's method here
sum = 0
for i in range(3):
    sum += max(sums)
    print(max(sums))
    sums.pop(sums.index(max(sums)))
    
print(sum)
