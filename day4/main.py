s: str = ""
with open("inp.txt", "r") as file:
    s = file.read()


LINES = s.split("\n")
LINES = [line for line in LINES if len(line) > 0]

def part1() -> int:
    res = 0
    for line in LINES:
        card, nums = line.split("|")
        card = card.split(":")[1]
        card = card.split(" ")
        card = [c for c in card if len(c) > 0]
        scard = set(card)
        nums = nums.split(" ")
        nums = [n for n in nums if len(n) > 0]
        snums = set(nums)
        val = len(snums & scard)
        res += (1 << (val - 1)) if val else 0
    return res

def part2() -> int:
    res = 0
    matches = {}
    for i, line in enumerate(LINES):
        card, nums = line.split("|")
        card = card.split(":")[1]
        card = card.split(" ")
        card = [c for c in card if len(c) > 0]
        scard = set(card)
        nums = nums.split(" ")
        nums = [n for n in nums if len(n) > 0]
        snums = set(nums)
        val = len(snums & scard)
        matches[i] = val

    scratchcards = {i: 1 for i in range(len(LINES))}
    for i in range(len(LINES)):
        for j in range(matches[i]):
            scratchcards[i + j + 1] += scratchcards[i]

    res = sum(scratchcards.values())
    return res

print("Part 1: ", part1())
print("Part 2: ", part2())
