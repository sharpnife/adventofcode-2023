import math
import functools

s: str = ""
with open("inp.txt", "r") as file:
    s = file.read()

LINES = list(filter(lambda x: len(x) > 0, s.split("\n")))

DIR = LINES[0].strip()

m = {
    line.split("=")[0].strip(): list(
        map(
            lambda x: x.strip(),
            line.split("=")[1].strip().removeprefix("(").removesuffix(")").split(","),
        )
    )
    for line in LINES[1:]
}


def part1() -> int:
    res = 0
    cur = "AAA"
    ind = 0
    while True:
        cur = m[cur][0] if DIR[ind] == "L" else m[cur][1]
        ind = (ind + 1) % len(DIR)
        res += 1
        if cur == "ZZZ":
            res += 1
            break
    return res


def part2() -> int:
    tot = []
    for k in m.keys():
        if k[-1] != "A":
            continue
        cur = k
        ind = 0
        res = 0
        while True:
            cur = m[cur][0] if DIR[ind] == "L" else m[cur][1]
            ind = (ind + 1) % len(DIR)
            res += 1
            if cur[-1] == "Z":
                tot.append(res)
                break
    return functools.reduce(math.lcm, tot)


print("Part 1: ", part1())
print("Part 2: ", part2())
