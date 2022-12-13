import math
import numpy
from collections import Counter

# sources:
#   https://github.com/iKevinY/advent/blob/master/2022/utils.py

def cmp3(a, b):
    """Three-way comparison aka spaceship operator (<=>)"""
    return [0, 1, -1][numpy.sign(a - b)]

def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def min_max_xy(points):
    """
    For a list of points, returns min_x, max_x, min_y, max_y.
    This works on tuples (x, y) and Point(x, y).
    """
    if len(points) == 0:
        return None, None, None, None
    if type(points[0]) == tuple:
        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_y = max(p[1] for p in points)
    else:
        min_x = min(p.x for p in points)
        max_x = max(p.x for p in points)
        min_y = min(p.y for p in points)
        max_y = max(p.y for p in points)

    return min_x, max_x, min_y, max_y

def print_grid(grid, f=None, quiet=False):
    """
    Outputs `grid` to stdout. This works whether `grid` is a 2D array,
    or a sparse matrix (dictionary) with keys either (x, y) or Point(x, y).
    This function also returns a tuple (a, b), where a is the serialized
    representation of the grid, in case what gets printed out to stdout
    needs to be consumed afterwards, and b is a Counter over the values
    in `grid`.
    Arguments:
        f: a function to transform the values of grid to something printable.
        quiet: don't output to stdout.
    Returns:
        List[String]: Serialized, printable version of the grid.
        Counter: The values contained in the grid.
    """
    if f is None:
        f = lambda x: str(x)  # NOQA

    counts = Counter()
    serialized = []

    if type(grid) is dict:
        positions = list(grid.keys())
        min_x, max_x, min_y, max_y = min_max_xy(positions)
        if type(positions[0]) is tuple:
            for y in range(min_y, max_y + 1):
                row = ''.join(f(grid.get((x, y), ' ')) for x in range(min_x, max_x + 1))
                if not quiet:
                    print(row)
                serialized.append(row)
                for c in row:
                    counts[c] += 1

        else:
            # (x, y) => point
            for y in range(min_y, max_y + 1):
                row = ''.join(f(grid.get(Point(x, y), ' ')) for x in range(min_x, max_x + 1))
                if not quiet:
                    print(row)
                serialized.append(row)
                for c in row:
                    counts[c] += 1
    else:
        min_x = 0
        min_y = 0
        for y in range(len(grid)):
            row = ''.join(f(grid[y][x]) for x in range(len(grid[0])))
            if not quiet:
                print(row)
            serialized.append(row)
            for x, c in enumerate(row):
                counts[c] += 1
                max_x = x
            max_y = y

    if not quiet:
        print("height={} ({} -> {})".format(max_y - min_y + 1, min_y, max_y))
        print("width={} ({} -> {})".format(max_x - min_x + 1, min_x, max_x))
        print("Statistics:")
        for item, num in counts.most_common():
            print("{}: {}".format(item, num))

    return serialized, counts

class Point:
    """Simple 2-dimensional point."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n)

    def __div__(self, n):
        return Point(self.x / n, self.y / n)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.length < other.length

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __hash__(self):
        return hash(tuple((self.x, self.y)))

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dist_manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def dist_chess(self, other):
        return max(abs(self.x - other.x), abs(self.y - other.y))

    def dist_chebyshev(self, other):
        return self.dist_chess(other)

    def angle(self, to=None):
        if to is None:
            return math.atan2(self.y, self.x)
        return math.atan2(self.y - to.y, self.x - to.x)

    def rotate(self, turns):
        """Returns the rotation of the Point around (0, 0) `turn` times clockwise."""
        turns = turns % 4

        if turns == 1:
            return Point(self.y, -self.x)
        elif turns == 2:
            return Point(-self.x, -self.y)
        elif turns == 3:
            return Point(-self.y, self.x)
        else:
            return self

    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    @property
    def chess(self):
        return max(abs(self.x), abs(self.y))

    @property
    def chebyshev(self):
        return self.chess

    @property
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def neighbours_4(self):
        return [self + p for p in DIRS_4]

    def neighbours(self):
        return self.neighbours_4()

    def neighbours_8(self):
        return [self + p for p in DIRS_8]

N = Point(0, 1)
NE = Point(1, 1)
E = Point(1, 0)
SE = Point(1, -1)
S = Point(0, -1)
SW = Point(-1, -1)
W = Point(-1, 0)
NW = Point(-1, 1)

DIRS_4 = DIRS = [
    Point(0, 1),   # north
    Point(1, 0),   # east
    Point(0, -1),  # south
    Point(-1, 0),  # west
]

DIRS_8 = [
    Point(0, 1),    # N
    Point(1, 1),    # NE
    Point(1, 0),    # E
    Point(1, -1),   # SE
    Point(0, -1),   # S
    Point(-1, -1),  # SW
    Point(-1, 0),   # W
    Point(-1, 1),   # NW
]
