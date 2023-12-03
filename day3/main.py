s: str = ""
with open("inp.txt", "r") as file:
    s = file.read()

LINES = s.split("\n")
LINES = [line for line in LINES if len(line) > 0]


def part1() -> int:
    ans = []
    for i, line in enumerate(LINES):
        flag = 0
        part_num = 0
        val = 0
        for j, char in enumerate(line):
            if char.isdigit():
                val = val * 10 + int(char)
                flag = 1
            else:
                if flag == 1 and part_num:
                    ans.append(val)
                val = 0
                part_num = 0
                flag = 0

            if flag == 1:
                di = [-1, -1, 0, 1, 1, 1, 0, -1]
                dj = [0, 1, 1, 1, 0, -1, -1, -1]

                for k in range(len(di)):
                    curi = i + di[k]
                    curj = j + dj[k]
                    if (
                        curi >= 0
                        and curi < len(LINES)
                        and curj >= 0
                        and curj < len(line)
                        and LINES[curi][curj] != "."
                        and not LINES[curi][curj].isdigit()
                    ):
                        part_num = 1
        if flag == 1 and part_num:
            ans.append(val)

    return sum(ans)


def part2() -> int:
    ans = []
    d = {}
    for i, line in enumerate(LINES):
        flag = 0
        part_num = 0
        stars = set()
        val = 0
        for j, char in enumerate(line):
            if char.isdigit():
                val = val * 10 + int(char)
                flag = 1
            else:
                if flag == 1 and part_num:
                    for s in stars:
                        p = d.setdefault(s, [])
                        p.append(val)
                val = 0
                part_num = 0
                stars = set()
                flag = 0

            if flag == 1:
                di = [-1, -1, 0, 1, 1, 1, 0, -1]
                dj = [0, 1, 1, 1, 0, -1, -1, -1]

                for k in range(len(di)):
                    curi = i + di[k]
                    curj = j + dj[k]
                    if (
                        curi >= 0
                        and curi < len(LINES)
                        and curj >= 0
                        and curj < len(line)
                        and LINES[curi][curj] != "."
                        and not LINES[curi][curj].isdigit()
                    ):
                        part_num = 1
                        if LINES[curi][curj] == "*":
                            stars.add(str(curi) + str(curj))
        if flag == 1 and part_num:
            for s in stars:
                p = d.setdefault(s, [])
                p.append(val)
    for v in d.values():
        if len(v) == 2:
            ans.append(v[0] * v[1])
    return sum(ans)


print("Part 1: ", part1())
print("Part 2: ", part2())
