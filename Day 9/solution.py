import sys

class Rope:
    knots = []
    visited = {}

    directions = {
        'U': (0, -1),
        'R': (1, 0),
        'D': (0, 1),
        'L': (-1, 0)
    }

    def __init__(self, knots: int):
        self.knots = [(0, 0) for node in range(knots)]
        self.visited = set(self.knots)

    def move(self, instruction: str):
        direction, distance = instruction.split()

        for s in range(int(distance)):
            self.knots[0] = self.compute_move(self.knots[0], self.directions[direction])
            for k in range(1, len(self.knots)):
                delta = [self.knots[k-1][i] - self.knots[k][i] for i in (0, 1)]
                if abs(max(delta, key = abs)) > 1:
                    self.knots[k] = self.compute_move(self.knots[k], [(x > 0) - (x < 0) for x in delta])
            self.visited.add(self.knots[-1])

    def compute_move(self, knot: tuple, move: tuple):
        return (knot[0] + move[0], knot[1] + move[1])

    def count_visited(self) -> int:
        return len(self.visited)

def prepare_data(input):
    return input.split('\n')

if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = prepare_data(open(file).read().strip())

    PartOne = Rope(2)
    for instruction in data:
        PartOne.move(instruction)
    print('Part 1:', PartOne.count_visited())

    PartTwo = Rope(10)
    for instruction in data:
        PartTwo.move(instruction)
    print('Part 2:', PartTwo.count_visited())
