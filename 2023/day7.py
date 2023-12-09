ordering = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
ordering2 = ["J", "1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
def value(h):
    hand = h[0]
    val = 0
    for i, l in enumerate(hand[::-1]):
        val += ordering.index(l) * (20 ** i)
    if hand.count(hand[0]) == 5:
        val += 60_000_000
    elif hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
        val += 50_000_000
    elif any(hand.count(hand[i]) == 3 for i in range(5)) and any(hand.count(hand[i]) == 2 for i in range(5)):
        val += 40_000_000
    elif any(hand.count(hand[i]) == 3 for i in range(5)):
        val += 30_000_000
    elif [hand.count(hand[i]) == 2 for i in range(5)].count(True) == 4:
        val += 20_000_000
    elif any(hand.count(hand[i]) == 2 for i in range(5)):
        val += 10_000_000
    return val

class joker:
    def __init__(self, v):
        self.v = v
        
    def __eq__(self, o):
        return self.v == o.v or self.v == "J" or o.v == "J"
    

def value2(h):
    hand = h[0]
    val = 0
    for i, l in enumerate(hand[::-1]):
        val += ordering2.index(l) * (20 ** i)
    hand2 = hand.replace("J", "")
    #hand = [joker(l) for l in hand]
    jokers = hand.count("J")
    if any(hand.count(c) == 5 for c in hand) or any(5 - jokers <= hand2.count(c) <= 5 for c in hand):
        val += 60_000_000
        return val
    if any(hand.count(c) == 4 for c in hand) or any(4 - jokers <= hand2.count(c) <= 4 for c in hand):
        val += 50_000_000
        return val
    # for full house
    # cannot have jokers as the two as it would already been picked up as a 4
    t = [hand.count(c) == 2 for c in hand].count(True)
    ys = any(hand.count(c) == 3 for c in hand)
    if ys and t == 2 or t == 4 and jokers == 1:
        val += 40_000_000
    elif any(3 - jokers <= hand.count(c) <= 3 for c in hand):
        val += 30_000_000
    elif [hand.count(c) == 2 for c in hand].count(True) == 4 or jokers == 1 and any(hand.count(c) == 2 for c in hand):
        val += 20_000_000
    elif any(hand.count(c) == 2 for c in hand) or jokers == 1:
        val += 10_000_000
    return val

import pprint
with open("2023/day7-input.txt", "r") as f:
    data = [k.split() for k in f.read().split("\n")]

    # part 1
    s = sorted(data, key=value)
    s1 = sum((i + 1) * int(k[1]) for i, k in enumerate(s))

    # part 2
    s = sorted(data, key=value2)
    s2 = sum((i + 1) * int(k[1]) for i, k in enumerate(s))
    [print(k, value2(k)) for k in s]
    pprint.pprint(s)
    print(value2(["12JJJ", 20]))
    print(s1, s2)
        
