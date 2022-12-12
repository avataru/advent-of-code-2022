import sys
sys.path.append('../')
from utils import Point
from collections import deque

class Map:
    grid = {}
    start = ''
    end = ''

    def __init__(self, lines: list):
        for x, line in enumerate(lines):
            for y, value in enumerate(line):
                if value == 'S':
                    self.start = Point(x, y)
                    value = 'a'
                elif value == 'E':
                    self.end = Point(x, y)
                    value = 'z'

                self.grid[Point(x, y)] = ord(value)

def get_path_length(map: Map) -> int:
    path = set()
    queue = deque([(map.start, 0)])

    while queue:
        point, depth = queue.popleft()
        if point in path:
            continue
        elif point == map.end:
            return depth

        path.add(point)

        for neighbour in point.neighbours():
            if neighbour not in map.grid:
                continue

            if map.grid[neighbour] - 1 <= map.grid[point]:
                queue.append((neighbour, depth + 1))

    return sys.maxsize

def part_one(map: Map) -> str:
    return get_path_length(map)

def part_two(map: Map) -> str:
    path = sys.maxsize
    for point in map.grid:
        if map.grid[point] == ord('a'):
            map.start = point
            current_path = get_path_length(map)
            path = current_path if current_path < path else path

    return path

def prepare_data(input):
    return input.splitlines()

if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = prepare_data(open(file).read().strip())

    map = Map(data)

    print('Part 1:', part_one(map))
    print('Part 2:', part_two(map))
