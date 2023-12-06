"""
Button time - X seconds
Distance - (T - X) * X 

(T - X) * X >= D
T*X - X*X >= D
T*X - X*X - D >= 0

T = 7
D = 9

7X - X^2 - 9 >= 0
-X^2 + 7X - 9 >= 0

(-7 +/- sqrt(49 - 4 * (-1) * (-9))) / 2*(-1)
(-7 +/- sqrt(49 - 36)) / 2*(-1)
(-7 +/- 3.6) / 2*(-1)

(-7 + 3.6) / -2
(-3.4)/-2 = 1.7

(-7 -3.6) / -2 = 5.3
"""
import math
from functools import reduce

s: str = ""
with open("inp.txt", "r") as file:
    s = file.read()

LINES = s.split("\n")
TIME = list(map(int, LINES[0].split(":")[1].split()))
DISTANCE = list(map(int, LINES[1].split(":")[1].split()))


def calc(times: list[int], distances: list[int]) -> int:
    res = 1
    for i in range(len(times)):
        T = times[i]
        D = distances[i]
        # T*X - X*X - D >= 0
        assert T * T >= 4 * D
        sqt = math.sqrt(T * T - 4 * D)

        x = (-T + sqt) / -2
        y = (-T - sqt) / -2

        xx = math.ceil(x) + (math.ceil(x) == x)
        yy = math.floor(y) - (math.floor(y) == y)
        res *= yy - xx + 1
    return res


def part1() -> int:
    return calc(TIME, DISTANCE)


def part2() -> int:
    time = int(reduce(lambda a, b: str(a) + str(b), TIME))
    distance = int(reduce(lambda a, b: str(a) + str(b), DISTANCE))
    return calc([time], [distance])


print("Part 1: ", part1())
print("Part 2: ", part2())
