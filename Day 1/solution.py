import sys

def prepare_data(input):
    calories = []
    for elf in input.split('\n\n'):
        calories.append(sum(int(calories) for calories in elf.split('\n')))
    return calories

def part_one(calories):
    return max(calories)

def part_two(calories):
    return sum(sorted(calories)[-3:])

if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = prepare_data(open(file).read().strip())

    print('Part 1: ' + str(part_one(data)))
    print('Part 2: ' + str(part_two(data)))
