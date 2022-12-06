import sys

def prepare_data(input):
    return input.split('\n')

def part_one(data):
    score = 0

    for round in data:
        elf, me = round.strip().split(' ')
        if elf == 'A' and me == 'X':
            score += 3 + 1
        elif elf == 'A' and me == 'Y':
            score += 6 + 2
        elif elf == 'A' and me == 'Z':
            score += 0 + 3
        elif elf == 'B' and me == 'X':
            score += 0 + 1
        elif elf == 'B' and me == 'Y':
            score += 3 + 2
        elif elf == 'B' and me == 'Z':
            score += 6 + 3
        elif elf == 'C' and me == 'X':
            score += 6 + 1
        elif elf == 'C' and me == 'Y':
            score += 0 + 2
        elif elf == 'C' and me == 'Z':
            score += 3 + 3

    return score

def part_two(data):
    score = 0

    for round in data:
        elf, result = round.strip().split(' ')
        if elf == 'A' and result == 'X':
            score += 0 + 3
        elif elf == 'A' and result == 'Y':
            score += 3 + 1
        elif elf == 'A' and result == 'Z':
            score += 6 + 2
        elif elf == 'B' and result == 'X':
            score += 0 + 1
        elif elf == 'B' and result == 'Y':
            score += 3 + 2
        elif elf == 'B' and result == 'Z':
            score += 6 + 3
        elif elf == 'C' and result == 'X':
            score += 0 + 2
        elif elf == 'C' and result == 'Y':
            score += 3 + 3
        elif elf == 'C' and result == 'Z':
            score += 6 + 1

    return score

if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = prepare_data(open(file).read().strip())

    print('Part 1: ' + str(part_one(data)))
    print('Part 2: ' + str(part_two(data)))
