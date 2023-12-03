inp: str = ""
with open("inp.txt", "r") as file:
    inp = file.read()

LINES = inp.split("\n")
LINES = [line for line in LINES if len(line) > 0]


def part1() -> int:
    res = 0
    for i, line in enumerate(LINES):
        count = {"red": 0, "green": 0, "blue": 0}
        for color in count.keys():
            ind = line.find(color)
            while ind >= 0:
                cur = ind
                while not line[cur].isdigit():
                    cur -= 1
                num = ""
                while line[cur].isdigit():
                    num += line[cur]
                    cur -= 1
                num = int("".join(reversed(num)))
                count[color] = max(count[color], num)
                ind = line.find(color, ind + 1)
        if not (count["red"] > 12 or count["green"] > 13 or count["blue"] > 14):
            res += i + 1
    return res


def part2() -> int:
    res = 0
    for line in LINES:
        count = {"red": 0, "green": 0, "blue": 0}
        for color in count.keys():
            ind = line.find(color)
            while ind >= 0:
                cur = ind
                while not line[cur].isdigit():
                    cur -= 1
                num = ""
                while line[cur].isdigit():
                    num += line[cur]
                    cur -= 1
                num = int("".join(reversed(num)))
                count[color] = max(count[color], num)
                ind = line.find(color, ind + 1)
        res += count["red"] * count["green"] * count["blue"]
    return res


print("Part 1: ", part1())
print("Part 2: ", part2())
