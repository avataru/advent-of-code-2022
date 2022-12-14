import sys
sys.path.append('../')
import copy

class Map:
    source = 500
    abyss_start = 0
    grid = set()

    def __init__(self, data: list):
        for line in data:
            x = [list(map(int, point.split(','))) for point in line.strip().split(' -> ')]
            for (x1, y1), (x2, y2) in zip(x, x[1:]):
                x1, x2 = sorted([x1, x2])
                y1, y2 = sorted([y1, y2])
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        self.grid.add(x + y * 1j)
                        self.abyss_start = max(self.abyss_start, y + 1)

    def simulate_endless_sand(self):
        grid = copy.deepcopy(self.grid)
        filled = 0
        while True:
            sand = self.source
            while True:
                if sand.imag >= self.abyss_start:
                    return filled
                if sand + 1j not in grid:
                    sand += 1j
                    continue
                if sand + 1j - 1 not in grid:
                    sand += 1j - 1
                    continue
                if sand + 1j + 1 not in grid:
                    sand += 1j + 1
                    continue
                grid.add(sand)
                filled += 1
                break
        return filled

    def simulate_sand(self):
        grid = copy.deepcopy(self.grid)
        filled = 0
        while self.source not in grid:
            sand = self.source
            while True:
                if sand.imag >= self.abyss_start:
                    break
                if sand + 1j not in grid:
                    sand += 1j
                    continue
                if sand + 1j - 1 not in grid:
                    sand += 1j - 1
                    continue
                if sand + 1j + 1 not in grid:
                    sand += 1j + 1
                    continue
                break
            grid.add(sand)
            filled += 1
        return filled


def part_one(map: Map):
    return map.simulate_endless_sand()

def part_two(map: Map):
    return map.simulate_sand()

def prepare_data(input):
    return input.splitlines()

if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = prepare_data(open(file).read().strip())

    map = Map(data)

    print('Part 1:', part_one(map))
    print('Part 2:', part_two(map))
