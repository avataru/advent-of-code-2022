import sys
import re

def prepare_data(input):
    return input.split('\n')

def part_one(data):
    overlap = 0
    for pair in data:
        elf_1_start, elf_1_end, elf_2_start, elf_2_end = map(int, re.findall(r'\d+', pair))

        if (elf_1_start <= elf_2_start and elf_1_end >= elf_2_end) or (elf_1_start >= elf_2_start and elf_1_end <= elf_2_end):
            overlap += 1

    return overlap

def part_two(data):
    overlap = 0
    for pair in data:
        elf_1_start, elf_1_end, elf_2_start, elf_2_end = map(int, re.findall(r'\d+', pair))

        if max(elf_1_start, elf_2_start) <= min(elf_1_end, elf_2_end):
            overlap += 1

    return overlap

if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = prepare_data(open(file).read().strip())

    print('Part 1: ' + str(part_one(data)))
    print('Part 2: ' + str(part_two(data)))
