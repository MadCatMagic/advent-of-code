# love globals in classes
toPulse = []
lowPulses = 0
highPulses = 0
class flipflop:
    def __init__(self, targets: list[str], name: str):
        self.state = False
        self.targets = targets
        self.name = name

    def pulse(self, signal: bool):
        if signal == False:
            self.state = not self.state
            for t in self.targets:
                toPulse.append((t, self.state, self.name))

    def __repr__(self):
        return f"%{1 if self.state else 0}->[{','.join(self.targets)}]"

class conjunction:
    # have to also initialise recordedStates
    def __init__(self, targets: list[str], name: str):
        self.targets = targets
        self.recordedStates = {}
        self.name = name

    def pulse(self, signal: True, origin: str):
        self.recordedStates[origin] = signal
        state = not (sum(int(v) for v in self.recordedStates.values()) == len(self.recordedStates))
        for target in self.targets:
            toPulse.append((target, state, self.name))

    def __repr__(self):
        return f"[{','.join(self.recordedStates.keys())}]->&->[{','.join(self.targets)}]"

def getData() -> tuple[list[str], dict[str, flipflop], dict[str, conjunction]]:
    with open("2023/day20-input.txt", "r") as f:
        fdata = f.read() + "\n&rx -> output"
        data = [[m.split(", ") if i > 0 else m for i, m in enumerate(l.split(" -> "))] for l in fdata.split("\n")]
        ffd = {}
        cjd = {}

        flipflops = {}
        conjunctions = {}

        for l in data:
            if l[0][0] == '%':
                ffd[l[0][1:]] = l[1]
            elif l[0][0] == '&':
                cjd[l[0][1:]] = l[1]
            else:
                broadcaster = l[1]

        for cj, ts in cjd.items():
            obj = conjunction(ts, cj)
            conjunctions[cj] = obj
        for cj, ts in cjd.items():
            for t in ts:
                if t in conjunctions:
                    conjunctions[t].recordedStates[cj] = False
        for ff, ts in ffd.items():
            obj = flipflop(ts, ff)
            flipflops[ff] = obj
            for t in ts:
                if t in conjunctions:
                    conjunctions[t].recordedStates[ff] = False
        for k in broadcaster:
            if k in conjunctions:
                conjunctions[k].recordedStates["broadcaster"] = False
        return broadcaster, flipflops, conjunctions

# part 1
broadcaster, flipflops, conjunctions = getData()
ticks = 0
while True:
    if toPulse == []:
        ticks += 1
        if ticks > 1000:
            break
        lowPulses += 1
        for v in broadcaster:
            toPulse.append((v, False, "broadcaster"))
    
    # pulse
    toPulseReal = toPulse[:]
    toPulse = []
    for name, p, origin in toPulseReal:
        if p: highPulses += 1
        else: lowPulses += 1
        if name in flipflops:
            flipflops[name].pulse(p)
        elif name in conjunctions:
            conjunctions[name].pulse(p, origin)

s1 = lowPulses * highPulses

# part 2
for ff in flipflops.values():
    ff.state = False
for cj in conjunctions.values():
    for k in cj.recordedStates.keys():
        cj.recordedStates[k] = False

activatesRX = list(conjunctions['rx'].recordedStates.keys())[0]
activationTimes = {}
ticks = 0
toPulse = []
while len(activationTimes) < 4:
    if toPulse == []:
        ticks += 1
        for v in broadcaster:
            toPulse.append((v, False, "broadcaster"))
    
    # pulse
    toPulseReal = toPulse[:]
    toPulse = []
    for name, p, origin in toPulseReal:
        if name in flipflops:
            flipflops[name].pulse(p)
        elif name in conjunctions:
            conjunctions[name].pulse(p, origin)
    if ticks > 5:
        for name, p, origin in toPulse:
            if name == activatesRX and p:
                activationTimes[origin] = ticks
from math import lcm
s2 = lcm(*activationTimes.values())

print(s1, s2)