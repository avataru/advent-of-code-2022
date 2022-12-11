import sys
from typing import Callable

class Monkey:
    operation: Callable[[int], int]
    check_factor: int
    check_true_target: int
    check_false_target: int

    items = []
    inspections = 0

    def __init__(self, definition: str):
        lines = definition.splitlines()

        self.items = list(map(int, lines[1][18:].split(', ')))

        operation = lines[2][19:]
        self.operation = eval(f'lambda old: {operation}')

        self.check_factor = int(lines[3][21:])
        self.check_true_target = int(lines[4][29:])
        self.check_false_target = int(lines[5][30:])

    def inspect(self, worry_factor: int, lcm = False) -> int:
        self.inspections += 1
        item = self.items.pop(0)
        item = self.operation(item)
        return item % worry_factor if lcm else item // worry_factor

    def test(self, item: int) -> int:
        return self.check_true_target if item % self.check_factor == 0 else self.check_false_target

def part_one(data: list) -> str:
    worry_factor = 3
    monkeys = []
    for monkey_definition in data:
        monkey = Monkey(monkey_definition)
        monkeys.append(monkey)

    return get_monkey_business(monkeys, 20, worry_factor, False)

def part_two(data: list) -> str:
    worry_factor = 1
    monkeys = []
    for monkey_definition in data:
        monkey = Monkey(monkey_definition)
        monkeys.append(monkey)
        worry_factor *= monkey.check_factor

    return get_monkey_business(monkeys, 10000, worry_factor, True)

def get_monkey_business(monkeys: list, rounds: int, worry_factor: int, lcm: bool) -> int:
    for _ in range(rounds):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.inspect(worry_factor, lcm)
                target = monkey.test(item)
                monkeys[target].items.append(item)

    inspections = sorted([monkey.inspections for monkey in monkeys], reverse = True)
    return inspections[0] * inspections[1]

def prepare_data(input):
    return input.split('\n\n')

if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = prepare_data(open(file).read().strip())

    print('Part 1:', part_one(data))
    print('Part 2:', part_two(data))
