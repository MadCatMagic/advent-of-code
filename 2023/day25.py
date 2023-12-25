import re
with open("2023/day25-input.txt", "r") as f:
    data = [(lambda x: (x[0], x[1:]))(re.findall("[a-z]+", s)) for s in f.read().splitlines()]
    network: dict[str, set[str]] = {}
    for ori, edges in data:
        if ori not in network:
            network[ori] = set()
        network[ori] = network[ori].union(set(edges))
        for e in edges:
            if e not in network:
                network[e] = set()
            network[e].add(ori)
    
    # add nodes to connected based on whichever nodes increase the connected edges by the least
    # when the connected edges == 3, break the loop as we have found the subgroup we need
    connected = {list(network)[0]}
    while sum(1 for node in connected for edge in network[node] if edge not in connected) > 3:
        connected.add(min(
            ((sum(-1 if edge in connected else 1 for edge in network[node]), node) 
             for node in network if node not in connected),
            key=lambda x: x[0]
        )[1])
    
    print(len(connected) * (len(network) - len(connected)))