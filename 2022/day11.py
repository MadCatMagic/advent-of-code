# no clue how to do fopen so just hard coding
monkeys = [{
    "items": [54, 98, 50, 94, 69, 62, 53, 85],
    "operation": lambda x: x * 13,
    "test": 3,
    "result": (2, 1)
}, {
    "items": [71, 55, 82],
    "operation": lambda x: x + 2,
    "test": 13,
    "result": (7, 2)
}, {
    "items": [77, 73, 86, 72, 87],
    "operation": lambda x: x + 8,
    "test": 19,
    "result": (4, 7)
}, {
    "items": [97, 91],
    "operation": lambda x: x + 1,
    "test": 17,
    "result": (6, 5)
}, {
    "items": [78, 97, 51, 85, 66, 63, 62],
    "operation": lambda x: x * 17,
    "test": 5,
    "result": (6, 3)
}, {
    "items": [88],
    "operation": lambda x: x + 3,
    "test": 7,
    "result": (1, 0)
}, {
    "items": [87, 57, 63, 86, 87, 53],
    "operation": lambda x: x * x,
    "test": 11,
    "result": (5, 0)
}, {
    "items": [73, 59, 82, 65],
    "operation": lambda x: x + 6,
    "test": 2,
    "result": (4, 3)
}]

# part 1
for monkey in monkeys:
    monkey["inspections"] = 0
for round in range(20):
    for monkey in monkeys:
        for item in monkey["items"]:
            v = monkey["operation"](item) / 3
            v = int(v)
            if v % monkey["test"] == 0:
                monkeys[monkey["result"][0]]["items"].append(v)
            else:
                monkeys[monkey["result"][1]]["items"].append(v)
            monkey["inspections"] += 1
        monkey["items"] = []

inspections = [monkey["inspections"] for monkey in monkeys]
inspections = sorted(inspections)
print(inspections[-1] * inspections[-2])

monkeys = [{
    "items": [54, 98, 50, 94, 69, 62, 53, 85],
    "operation": lambda x: x * 13,
    "test": 3,
    "result": (2, 1)
}, {
    "items": [71, 55, 82],
    "operation": lambda x: x + 2,
    "test": 13,
    "result": (7, 2)
}, {
    "items": [77, 73, 86, 72, 87],
    "operation": lambda x: x + 8,
    "test": 19,
    "result": (4, 7)
}, {
    "items": [97, 91],
    "operation": lambda x: x + 1,
    "test": 17,
    "result": (6, 5)
}, {
    "items": [78, 97, 51, 85, 66, 63, 62],
    "operation": lambda x: x * 17,
    "test": 5,
    "result": (6, 3)
}, {
    "items": [88],
    "operation": lambda x: x + 3,
    "test": 7,
    "result": (1, 0)
}, {
    "items": [87, 57, 63, 86, 87, 53],
    "operation": lambda x: x * x,
    "test": 11,
    "result": (5, 0)
}, {
    "items": [73, 59, 82, 65],
    "operation": lambda x: x + 6,
    "test": 2,
    "result": (4, 3)
}]

# part 2
mod = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
for monkey in monkeys:
    monkey["inspections"] = 0
for round in range(10000):
    for monkey in monkeys:
        for item in monkey["items"]:
            v = monkey["operation"](item)
            if v % monkey["test"] == 0:
                monkeys[monkey["result"][0]]["items"].append(v)
            else:
                monkeys[monkey["result"][1]]["items"].append(v)
            monkey["inspections"] += 1
        monkey["items"] = []
    for monkey in monkeys:
        for i, v in enumerate(monkey["items"]):
            monkey["items"][i] = v % mod

inspections = [monkey["inspections"] for monkey in monkeys]
inspections = sorted(inspections)
print(inspections[-1] * inspections[-2])