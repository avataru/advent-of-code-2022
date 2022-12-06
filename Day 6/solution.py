import sys

def prepare_data(input):
    return input

def part_one(data):
    return find_marker(data, 4)

def part_two(data):
    return find_marker(data, 14)

def find_marker(data, length):
    for i in range(0, len(data[:1 - length])):
        if is_marker(data[i:i + length]):
            return i + length
        i += 1

def is_marker(string):
    return len(set(string)) == len(string)

if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = prepare_data(open(file).read().strip())

    print('Part 1: ' + str(part_one(data)))
    print('Part 2: ' + str(part_two(data)))
