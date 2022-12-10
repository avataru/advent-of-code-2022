import sys

class Device:
    x = 1
    cycle = 0
    signal_strength = 0
    screen = []

    def __init__(self):
        self.screen = [['' for column in range(40)] for row in range(6)]

    def execute(self, instruction: str):
        command = instruction[:4]
        value = instruction[5:]

        if command == 'noop':
            self.tick()

        elif command == 'addx':
            self.tick()
            self.tick()
            self.x += int(value)

    def tick(self):
        self.screen[self.cycle // 40][self.cycle % 40] = '█' if abs(self.x - (self.cycle % 40)) <= 1 else ' '
        if self.is_signal_cycle():
            self.signal_strength += self.x * self.cycle
        self.cycle += 1

    def is_signal_cycle(self) -> bool:
        return True if self.cycle % 20 == 0 and (self.cycle / 20 + 1) % 2 == 0 else False

def prepare_data(input):
    return input.split('\n')

if __name__ == '__main__':
    file = ('sample' if len(sys.argv) > 1 and sys.argv[1] in ['-s', '--sample'] else 'input') + '.txt'
    data = prepare_data(open(file).read().strip())

    ElvenDevice = Device()

    for instruction in data:
        ElvenDevice.execute(instruction)

    print('Part 1:', ElvenDevice.signal_strength)

    print('Part 2:')
    for row in range(6):
        print(''.join(ElvenDevice.screen[row]))


