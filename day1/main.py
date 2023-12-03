from itertools import dropwhile

inp: str = ""
with open("inp.txt", "r") as file:
    inp = file.read()

LINES = inp.split("\n")
LINES = [line for line in LINES if len(line) > 0]


def part1() -> int:
    res = 0
    for line in LINES:
        if len(line) == 0:
            continue
        pre = list(dropwhile(lambda x: ord(x) < ord("0") or ord(x) > ord("9"), line))
        suf = list(
            dropwhile(lambda x: ord(x) < ord("0") or ord(x) > ord("9"), reversed(line))
        )
        res += int(pre[0] + suf[0])
    return res


def part2() -> int:
    NUM = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    def calc(line: str, rev: bool = False) -> int:
        dig = -1
        bst = 1e9
        for digit, word in NUM.items():
            ind1 = line.find(str(digit))
            ind2 = line.find(word if not rev else "".join(reversed(word)))
            if ind1 < 0:
                ind1 = 1e9
            if ind2 < 0:
                ind2 = 1e9
            ind = min(ind1, ind2)
            if ind < bst:
                bst = ind
                dig = digit
        return dig

    res = 0
    for _line in LINES:
        res += calc(_line) * 10 + calc("".join(reversed(_line)), True)
    return res


print("Part 1: ", part1())
print("Part 2: ", part2())
