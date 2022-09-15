import re

with open('day_05/lines.txt') as f:
    line_strings = f.readlines()


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.start_point = (self.x1, self.y1)
        self.end_point = (self.x2, self.y2)

    def is_vertical(self):
        return self.x1 == self.x2

    def is_horizontal(self):
        return self.y1 == self.y2

    def __str__(self):
        return f'({self.x1},{self.y1}) -> ({self.x2},{self.y2})'

    def __repr__(self):
        return self.__str__()


lines = []
for line in line_strings:
    if line_search := re.search(r'(\d+),(\d+) -> (\d+),(\d+)\n?', line):
        lines.append(Line(*line_search.groups()))

# part 1
h_and_v_lines = [line for line in lines if line.is_vertical() or line.is_horizontal()]
points = {}
for line in h_and_v_lines:
    points.setdefault(line.end_point, 0)
    points[line.end_point] += 1
    for x in range(line.x1, line.x2, 1 if line.x2 >= line.x1 else -1):
        points.setdefault((x, line.y1), 0)
        points[(x, line.y1)] += 1
    for y in range(line.y1, line.y2, 1 if line.y2 >= line.y1 else -1):
        points.setdefault((line.x1, y), 0)
        points[(line.x1, y)] += 1
print(len([x for x in points.values() if x > 1]))

# part 2 consider diagonal lines
diag_lines = [line for line in lines if not line.is_horizontal() and not line.is_vertical()]
for line in diag_lines:
    for i in range(abs(line.x1 - line.x2) + 1):
        x_dir = 1 if line.x2 > line.x1 else -1
        y_dir = 1 if line.y2 > line.y1 else -1
        pt = line.x1 + (i * x_dir), line.y1 + (i * y_dir)
        points.setdefault(pt, 0)
        points[pt] += 1

print(len([x for x in points.values() if x > 1]))
