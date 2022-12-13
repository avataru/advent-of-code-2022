import sys
sys.path.append('../')
from functools import cmp_to_key

def compare(left, right) -> int:
    if not isinstance(left, list):
        left = [left]

    if not isinstance(right, list):
        right = [right]

    for i in range(min(len(left), len(right))):
        if isinstance(left[i], list) or isinstance(right[i], list):
            result = compare(left[i], right[i])
            if result != 0:
                return result
        elif left[i] < right[i]:
            return -1
        elif left[i] > right[i]:
            return 1

    if len(left) < len(right):
        return -1

    if len(left) > len(right):
        return 1

    return 0

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
