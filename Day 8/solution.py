import sys

def prepare_data(input):
    return input.split('\n')

def part_one(data):
    width = len(data[0])
    height = len(data)
    visible = 2 * height + 2 * width - 4

    y = 1
    for line in data[1:-1]:
        for x in range(1, width - 1):
            column = get_column(x, data)
            if is_visible_horizontally(x, line) or is_visible_vertically(y, column):
                visible += 1
        y += 1

    return visible

def part_two(data):
    width = len(data[0])
    height = len(data)
    best_score = 0

    y = 0
    for line in data:
        for x in range(0, width):
            column = get_column(x, data)
            tree = int(line[x])
            scenic_score = get_scenic_score(tree, x, y, list(line), column)
            best_score = scenic_score if scenic_score > best_score else best_score
        y += 1

    return best_score

def is_visible(tree, trees):
    return max(trees) < tree

def get_before(coord, line):
    return map(int, line[:coord])

def get_after(coord, line):
    return map(int, line[coord + 1:])

def is_visible_horizontally(x, line):
    tree = int(line[x])
    return is_visible(tree, get_before(x, line)) or is_visible(tree, get_after(x, line))

def get_column(x, data):
    column = []
    for line in data:
        column.append(line[x])
    return column

def is_visible_vertically(y, column):
    tree = int(column[y])
    return is_visible(tree, get_before(y, column)) or is_visible(tree, get_after(y, column))

def get_scenic_score(tree, x, y, line, column):
    west_score = calculate_scenic_score(tree, list(get_before(x, line))[::-1])
    east_score = calculate_scenic_score(tree, list(get_after(x, line)))
    north_score = calculate_scenic_score(tree, list(get_before(y, list(column)))[::-1])
    south_score = calculate_scenic_score(tree, list(get_after(y, column)))
    return west_score * east_score * north_score * south_score

def calculate_scenic_score(tree, trees):
    score = 0
    for t in trees:
        score += 1 if t < tree else 0
        if t >= tree:
            score += 1
            break

    return score


if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = prepare_data(open(file).read().strip())

    print('Part 1: ' + str(part_one(data)))
    print('Part 2: ' + str(part_two(data)))
