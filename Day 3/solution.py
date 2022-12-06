import sys

def prepare_data(input):
    return input.split('\n')

def part_one(data):
    value = 0

    for line in data:
        first_rucksack, second_rucksack = line[:len(line) // 2], line[len(line) // 2:]
        items = list(set(first_rucksack) & set(second_rucksack))

        for item in items:
            value += get_item_value(item)

    return value


def part_two(data):
    value = 0

    for group in chunks(data, 3):
        items = list(set(group[0]) & set(group[1]) & set(group[2]))

        for item in items:
            value += get_item_value(item)

    return value

def get_item_value(item):
    value = ord(item)
    return value - ord('A') + 27 if value < ord('a') else value - ord('a') + 1


def chunks(list, size):
    for i in range(0, len(list), size):
        yield list[i:i + size]

if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = prepare_data(open(file).read().strip())

    print('Part 1: ' + str(part_one(data)))
    print('Part 2: ' + str(part_two(data)))
