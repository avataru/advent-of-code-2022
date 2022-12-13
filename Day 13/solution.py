import sys
sys.path.append('../')
from utils import cmp3
from functools import cmp_to_key

def compare(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return cmp3(left, right)

    left = [left] if isinstance(left, int) else left
    right = [right] if isinstance(right, int) else right

    while len(left) > 0 and len(right) > 0:
        c = compare(left.pop(0), right.pop(0))
        if c != 0:
            return c

    if len(left) == 0 and len(right) == 0:
        return 0
    elif len(left) == 0:
        return -1
    elif len(right) == 0:
        return 1

    raise Exception(f'Invalid input: left = {left} and right = {right}')

def part_one(data: str) -> str:
    packets = [[eval(v) for v in pair.splitlines()] for pair in data.split('\n\n')]
    return sum(i + 1 for i, (p1, p2) in enumerate(packets) if compare(p1, p2) < 0)

def part_two(data: str) -> str:
    packets = [eval(v) for v in data.splitlines() if len(v) > 0]
    divider_1, divider_2 = [[[2]], [[6]]]
    packets.extend([divider_1, divider_2])
    packets = sorted(packets, key=cmp_to_key(compare))
    return((packets.index(divider_1) + 1) * (packets.index(divider_2) + 1))

if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = open(file).read().strip()

    print('Part 1:', part_one(data))
    print('Part 2:', part_two(data))
