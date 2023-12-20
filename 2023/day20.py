

with open("2023/day20-input.txt", "r") as f:
    data = [[m.split(", ") if i > 0 else m for i, m in enumerate(l.split(" -> "))] for l in f.read().split("\n")]
    broadcaster = None
    ffd = {}
    cjd = {}

    # love globals in classes
    toPulse = []
    lowPulses = 0
    highPulses = 0
    class flipflop:
        def __init__(self, target):
            self.state = False
            self.target = target

        def pulse(self, signal: bool):
            global highPulses, lowPulses
            if signal == False:
                self.state = not self.state
                if self.state: highPulses += 1
                else: lowPulses += 1
                toPulse.append((self.target, self.state))

        def __repr__(self):
            return f"%{1 if self.state else 0}->{self.target}"

    class conjunction:
        # have to also initialise recordedStates
        def __init__(self, targets: list[str]):
            self.targets = targets
            self.recordedStates = {}

        def pulse(self, signal: True, origin: str):
            global highPulses, lowPulses
            self.recordedStates[origin] = signal
            state = not sum(self.recordedStates.values()) == len(self.recordedStates)
            if state: highPulses += len(self.targets)
            else: lowPulses += len(self.targets)
            for target in self.targets:
                toPulse.append((target, state))

        def __repr__(self):
            return f"[{','.join(self.recordedStates.keys())}]->&->[{','.join(self.targets)}]"

    for l in data:
        if l[0][0] == '%':
            ffd[l[0][1:]] = l[1][0]
        elif l[0][0] == '&':
            cjd[l[0][1:]] = l[1]
        else:
            broadcaster = l[1]

    flipflops = {}
    conjunctions = {}
    for cj, ts in cjd.items():
        obj = conjunction(ts)
        conjunctions[cj] = obj
    for ff, t in ffd.items():
        obj = flipflop(t)
        flipflops[ff] = obj
        if t in conjunctions:
            conjunctions[t].recordedStates[ff] = False
    
    ticks = 0
    while ticks < 1000:
        if toPulse == []:
            for v in broadcaster:
                toPulse.append((v, False))
                lowPulses += 1
            ticks += 1
        
        # pulse
        toPulseReal = toPulse[:]
        toPulse = []
        for name, p in toPulseReal:
            if name in flipflops:
                flipflops[name].pulse(p)
            elif name in conjunctions:
                conjunctions[name].pulse(p, name)
        
    s1 = lowPulses * highPulses
    print(s1)