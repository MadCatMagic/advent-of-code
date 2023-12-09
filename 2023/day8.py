import math

def run(node, network, cond):
    s1 = 0
    index = 0
    while cond(node):
        s1 += 1
        node = network[node][0 if instr[index] == "L" else 1]
        index += 1
        index %= len(instr)
    return s1

with open("2023/day8-input.txt", "r") as f:
    data = f.read().split("\n\n")
    instr = data[0]
    nodes = [node.split(" = ") for node in data[1].split("\n")]
    network = {node[0]: (node[1][1:4], node[1][6:9]) for node in nodes}
    
    # part 1
    s1 = run("AAA", network, lambda x: x != "ZZZ")
    
    # part 2
    nodes = [node for node in network.keys() if node[2] == "A"]
    s2 = math.lcm(*[run(node, network, lambda x: x[2] != "Z") for node in nodes])

    print(s1, s2)