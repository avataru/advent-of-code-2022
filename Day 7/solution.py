import sys

def prepare_data(input):
    dirs = {'/': 0}
    path = []

    for line in input.splitlines():
        if line.startswith('$ cd /'):
            path = []

        elif line.startswith('$ cd ..'):
            path.pop()

        elif line.startswith('$ cd'):
            path.append('/'.join(path) + '/' + line[5:])

        elif line.startswith('$ ls'):
            continue

        elif line.startswith('dir'):
            dirs['/'.join(path) + '/' + line[4:]] = 0

        else:
            size, name = line.split()
            size = int(size)

            dirs['/'] += size
            for dir in path:
                dirs[dir] += size

    return dirs


def part_one(dirs):
    return sum(size for size in dirs.values() if size <= 100000)

def part_two(dirs):
    required_size = 30000000 - (70000000 - dirs['/'])
    return min(size for size in dirs.values() if size >= required_size)

if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = prepare_data(open(file).read().strip())

    print('Part 1: ' + str(part_one(data)))
    print('Part 2: ' + str(part_two(data)))
