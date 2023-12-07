from functools import cmp_to_key

s: str = ""
with open("inp.txt", "r") as file:
    s = file.read()

LINES = list(filter(lambda x: len(x) > 0, s.split("\n")))

CARDS = list(
    map(
        lambda x: (x[0], int(x[1])),
        [tuple(map(str, line.split(" "))) for line in LINES],
    )
)

order = {}


def cmp(x, y):
    if x[0] == y[0]:
        for i, c in enumerate(x[1]):
            if order[c] < order[y[1][i]]:
                return 1
            elif order[c] > order[y[1][i]]:
                return -1
    return -1 if x[0] < y[0] else 1


def part1() -> int:
    global order
    order = {
        "A": 1,
        "K": 2,
        "Q": 3,
        "J": 4,
        "T": 5,
    } | {str(p): 6 + i for i, p in enumerate(list(range(9, 1, -1)))}
    sorted = []
    for card, bid in CARDS:
        st = set(card)
        sz = []
        for val in st:
            sz.append(card.count(val))
        sz.sort()
        if sz == [5]:
            sorted.append((7, card, bid))
        elif sz == [1, 4]:
            sorted.append((6, card, bid))
        elif sz == [2, 3]:
            sorted.append((5, card, bid))
        elif sz == [1, 1, 3]:
            sorted.append((4, card, bid))
        elif sz == [1, 2, 2]:
            sorted.append((3, card, bid))
        elif sz == [1, 1, 1, 2]:
            sorted.append((2, card, bid))
        elif sz == [1, 1, 1, 1, 1]:
            sorted.append((1, card, bid))

    sorted.sort(key=cmp_to_key(cmp))

    res = 0
    for i in range(len(sorted)):
        res += (i + 1) * sorted[i][2]

    return res


def part2() -> int:
    global order
    order = (
        {
            "A": 1,
            "K": 2,
            "Q": 3,
            "T": 4,
        }
        | {str(p): 5 + i for i, p in enumerate(list(range(9, 1, -1)))}
        | {"J": 13}
    )

    sorted = []
    for card, bid in CARDS:
        st = set(card)
        sz = []
        for val in st:
            sz.append(card.count(val))
        sz.sort()
        if "J" in st:
            tot = card.count("J")
            sz[sz.index(tot)] = 0
            sz.sort()
            sz.reverse()
            cur = 0
            while tot > 0:
                x = min(5 - sz[cur], tot)
                tot -= x
                sz[cur] += x
                cur += 1
            sz.sort()
            if sz[0] == 0:
                sz.remove(0)
        if sz == [5]:
            sorted.append((7, card, bid))
        elif sz == [1, 4]:
            sorted.append((6, card, bid))
        elif sz == [2, 3]:
            sorted.append((5, card, bid))
        elif sz == [1, 1, 3]:
            sorted.append((4, card, bid))
        elif sz == [1, 2, 2]:
            sorted.append((3, card, bid))
        elif sz == [1, 1, 1, 2]:
            sorted.append((2, card, bid))
        elif sz == [1, 1, 1, 1, 1]:
            sorted.append((1, card, bid))

    sorted.sort(key=cmp_to_key(cmp))

    res = 0
    for i in range(len(sorted)):
        res += (i + 1) * sorted[i][2]

    return res


print("Part 1: ", part1())
print("Part 2: ", part2())
