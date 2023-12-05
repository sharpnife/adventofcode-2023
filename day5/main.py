import copy

s: str = ""
with open("inp.txt", "r") as file:
    s = file.read()

LINES = s.split("\n")
LINES = [line for line in LINES if len(line) > 0]

SEEDS = [int(seed) for seed in LINES[0].split(":")[1].split()]


def part1() -> int:
    seeds = copy.deepcopy(SEEDS)
    mapped_seeds = []
    for i in range(2, len(LINES)):
        if LINES[i].find("map") > -1:
            for seed in seeds:
                mapped_seeds.append(seed)
            seeds = copy.deepcopy(mapped_seeds)
            mapped_seeds = []
        else:
            dest, src, ran = [int(l) for l in LINES[i].split(" ") if len(l) > 0]
            rm = []
            for seed in seeds:
                if src <= seed < (src + ran):
                    rm.append(seed)
                    mapped_seeds.append(dest + seed - src)
            for seed in rm:
                seeds.remove(seed)

    for seed in seeds:
        mapped_seeds.append(seed)
    seeds = copy.deepcopy(mapped_seeds)
    return min(seeds)


def part2():
    seeds = [(SEEDS[i], SEEDS[i] + SEEDS[i + 1] - 1) for i in range(0, len(SEEDS), 2)]
    mapped_seeds = []
    for i in range(2, len(LINES)):
        if LINES[i].find("map") > -1:
            for seed in seeds:
                mapped_seeds.append(seed)
            seeds = copy.deepcopy(mapped_seeds)
            mapped_seeds = []
        else:
            dest, src, ran = [int(l) for l in LINES[i].split(" ") if len(l) > 0]
            rm = []
            ext = []
            for start, end in seeds:
                if src <= start < (src + ran):
                    diff = start - src
                    mend = min(end, src + ran - 1)
                    mapped_seeds.append((dest + diff, dest + diff + mend - start))
                    if mend < end:
                        ext.append((mend + 1, end))
                    rm.append((start, end))
                elif src <= end < (src + ran):
                    mapped_seeds.append((dest, dest + end - src))
                    ext.append((start, src - 1))
                    rm.append((start, end))
            for val in rm:
                seeds.remove(val)
            for val in ext:
                seeds.append(val)

    for seed in seeds:
        mapped_seeds.append(seed)
    seeds = copy.deepcopy(mapped_seeds)
    res = 1e18
    for start, end in seeds:
        assert start <= end
        res = min(res, start)
    return res


print("Part 1: ", part1())
print("Part 2: ", part2())
