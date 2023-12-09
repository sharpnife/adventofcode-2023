import copy

s: str = ""
with open("inp.txt", "r") as file:
    s = file.read()

LINES = s.splitlines()

values = []

for line in LINES:
    cur = list(map(int, line.split(" ")))
    arr = []
    while True:
        arr.append(copy.deepcopy(cur))
        nxt = []
        for i in range(len(cur) - 1):
            nxt.append(cur[i + 1] - cur[i])
        cur = nxt
        if len(set(cur)) == 1 and next(iter(set(cur))) == 0:
            arr.append(copy.deepcopy(cur))
            break
    values.append(arr)


def part1() -> int:
    res = 0
    for a in range(len(values)):
        cur = 0
        for i in range(-1, -len(values[a]) - 1, -1):
            cur += values[a][i][-1]
        res += cur
    return res


def part2() -> int:
    res = 0
    for a in range(len(values)):
        cur = 0
        for i in range(-1, -len(values[a]) - 1, -1):
            cur = values[a][i][0] - cur
        res += cur
    return res


print("Part 1: ", part1())
print("Part 2: ", part2())
