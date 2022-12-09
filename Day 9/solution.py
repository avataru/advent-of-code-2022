import sys

def prepare_data(input):
    return input.split('\n')

def part_one(data):
    visited = {}
    head_position, tail_position = [[0, 0], [0, 0]]

    for instruction in data:
        for step in parse_move(instruction):
            head_position = move(head_position, step)
            tail_position = move_tail(head_position, tail_position, step)
            visited[','.join(map(str, tail_position))] = True

    return len(visited)

def part_two(data):
    # TO DO
    return ''

def move(position: list, step: list) -> list:
    return [x + y for x, y in zip(position, step)]

def move_tail(head_position: list, tail_position: list, step: list) -> list:
    distance = get_distance(head_position, tail_position)

    if distance == 0:
        return tail_position

    else:
        tail_position = [head_position[0], tail_position[1]] if step[1] != 0 else [tail_position[0], head_position[1]]
        return move(tail_position, step)

def parse_move(move: str) -> list:
    direction, distance = move.split()
    distance = int(distance)
    steps = []

    for step in range(0, distance):
        if direction == 'U':
            steps.append([0, -1])
        elif direction == 'R':
            steps.append([1, 0])
        elif direction == 'D':
            steps.append([0, 1])
        elif direction == 'L':
            steps.append([-1, 0])

    return steps

def get_distance(head_position: list, tail_position: list) -> int:
    horizontal_distance = abs(head_position[0] - tail_position[0])
    vertical_distance = abs(head_position[1] - tail_position[1])

    # overlapping
    if horizontal_distance == 0 and vertical_distance == 0:
        return 0

    # orthogonally adjacent
    elif horizontal_distance + vertical_distance == 1:
        return 0

    # diagonally adjacent
    elif horizontal_distance == vertical_distance:
        return 0

    # distance
    else:
        return horizontal_distance + vertical_distance - 1


if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = prepare_data(open(file).read().strip())

    print('Part 1: ' + str(part_one(data)))
    print('Part 2: ' + str(part_two(data)))
