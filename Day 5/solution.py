import sys
import re

def prepare_data(input):
    data, moves = input.split('\n\n')

    crates = []
    data = data.splitlines()[:-1]
    for line in data:
        matches = re.findall(r'(\s{3}|\[[A-Z]\])\s?', line)
        matches = [m.strip('[ ]') for m in matches]
        crates.append(matches)

    stacks_count = len(crates[0])
    stacks = [''] * stacks_count
    for s in range(stacks_count):
        for row in reversed(crates):
            stacks[s] += row[s]

    return [stacks, moves]

def part_one(stacks, moves):
    for instruction in moves.splitlines():
        quantity, source, destination = parse_move(instruction)

        crates = stacks[int(source) - 1][int(quantity) * -1:]
        stacks[int(source) - 1] = stacks[int(source) - 1][:int(quantity) * -1]
        stacks[int(destination) - 1] += crates[::-1]

    return ''.join(map(lambda c: c[-1], stacks))

def part_two(stacks, moves):
    for instruction in moves.splitlines():
        quantity, source, destination = parse_move(instruction)

        crates = stacks[int(source) - 1][int(quantity) * -1:]
        stacks[int(source) - 1] = stacks[int(source) - 1][:int(quantity) * -1]
        stacks[int(destination) - 1] += crates

    return ''.join(map(lambda c: c[-1], stacks))

def parse_move(instruction):
    return re.findall(r'\d+', instruction)

if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    stacks, moves = prepare_data(open(file).read())

    print('Part 1: ' + str(part_one(stacks.copy(), moves)))
    print('Part 2: ' + str(part_two(stacks.copy(), moves)))
