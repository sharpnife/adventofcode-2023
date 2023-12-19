# Warning: It's a terrible implementation ... well it gets the job done, so ig I'm satisfied lol
import attrs
import copy
from itertools import takewhile

s: str = ""
with open("inp.txt", "r") as file:
    s = file.read()

LINES = s.splitlines()

w = list(takewhile(lambda x: len(x) > 0, LINES))
x = LINES[len(w) + 1 :]

d = {}


@attrs.define
class Edge:
    frm: str = "."
    sign: str = "."
    val: int = -1
    to: str = "."


@attrs.define
class X:
    x: int
    m: int
    a: int
    s: int


def fun(v: str) -> Edge:
    if len(v.split(":")) > 1:
        p = v.split(":")
        sign = p[0][max(p[0].find("<"), p[0].find(">"))]
        assert sign == ">" or sign == "<"
        return Edge(
            frm=p[0].split(sign)[0], sign=sign, val=int(p[0].split(sign)[-1]), to=p[-1]
        )
    return Edge(to=v)


for i in w:
    k = i.split("{")[0]
    v = filter(lambda x: len(x) > 0, i[i.find("{") + 1 : -1].split(","))
    v = list(map(fun, v))
    d[k] = v

xs = []
for i in x:
    v = []
    for k in i[1:-1].split(","):
        v.append(int(k.split("=")[-1]))
    xs.append(X(x=v[0], m=v[1], a=v[2], s=v[3]))


def part1():
    res = 0
    for x in xs:
        cur = "in"
        while True:
            for v in d[cur]:
                if v.frm == ".":
                    cur = v.to
                    break
                else:
                    nxt = ""
                    assert v.frm != "." and v.sign != "."
                    match v.frm:
                        case "x":
                            if v.sign == ">":
                                if x.x > v.val:
                                    nxt = v.to
                            elif v.sign == "<":
                                if x.x < v.val:
                                    nxt = v.to
                            else:
                                assert False
                        case "m":
                            if v.sign == ">":
                                if x.m > v.val:
                                    nxt = v.to
                            elif v.sign == "<":
                                if x.m < v.val:
                                    nxt = v.to
                            else:
                                assert False
                        case "a":
                            if v.sign == ">":
                                if x.a > v.val:
                                    nxt = v.to
                            elif v.sign == "<":
                                if x.a < v.val:
                                    nxt = v.to
                            else:
                                assert False
                        case "s":
                            if v.sign == ">":
                                if x.s > v.val:
                                    nxt = v.to
                            elif v.sign == "<":
                                if x.s < v.val:
                                    nxt = v.to
                            else:
                                assert False
                        case _:
                            assert False
                    if nxt != "":
                        cur = nxt
                        break
            if cur == "R":
                break
            if cur == "A":
                res += x.x + x.m + x.a + x.s
                break
    return res


def rec(node: str, mx: tuple[int, int, int, int], mn: tuple[int, int, int, int]) -> int:
    nmn = list(mn)
    nmx = list(mx)
    res = 0
    for v in d[node]:
        if v.frm == ".":
            # leaf node
            if v.to == "A":
                ret = 1
                for i in range(4):
                    ret *= nmx[i] - nmn[i] + 1
                res += ret
            elif v.to == "R":
                pass
            else:
                res += rec(v.to, tuple(nmx), tuple(nmn))
            break
        else:
            dnmn = copy.deepcopy(nmn)
            dnmx = copy.deepcopy(nmx)
            p = ["x", "m", "a", "s"].index(v.frm)
            if v.sign == ">":
                nmn[p] = max(nmn[p], v.val + 1)
                dnmx[p] = min(nmx[p], v.val)
            elif v.sign == "<":
                nmx[p] = min(nmx[p], v.val - 1)
                dnmn[p] = max(nmn[p], v.val)
            else:
                assert False

            bad = 0
            for i in range(4):
                if nmn[i] > nmx[i]:
                    bad = 1
                    break
            if bad:
                break

            if v.to == "A":
                ret = 1
                for i in range(4):
                    ret *= nmx[i] - nmn[i] + 1
                res += ret
            elif v.to == "R":
                pass
            else:
                res += rec(v.to, tuple(nmx), tuple(nmn))
            nmn = dnmn
            nmx = dnmx
    return res


def part2():
    return rec("in", mn=(1, 1, 1, 1), mx=(4000, 4000, 4000, 4000))


print("Part 1: ", part1())
print("Part 2: ", part2())
