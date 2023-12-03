import re
from functools import reduce

lines = open("input.txt", "r").read().splitlines()
total_lines = len(lines)
symbols = set()

symbols = set(c for line in lines for c in line if not c.isdigit() and c!='.')
symbols = "".join(sorted(list(symbols), key = lambda x:1 if x=="-" else 0))

def is_symbol(s):
  return re.match(f"[{symbols}]", s) is not None

def generate_coords(x,y, xmax, ymax):
  coords = [
      (i,j) for i in range(max(x-1, 0), min(x+1, xmax) + 1)
        for j in range(max(y-1, 0), min(y+1, ymax) + 1)
          if not (i == x and j == y)
  ]
  return coords

def check_for_symbol(cn, ln, num_characters, num_lines):
  return any([is_symbol(lines[y][x]) for (x, y) in generate_coords(cn, ln, num_characters-1, num_lines-1)])

valid = []
total_lines = len(lines)
for ln, line in enumerate(lines):
  current = []
  for cn,c in enumerate(line):
    if c.isdigit():
      current.append((int(c), cn))
    if current and ((cn == len(line) - 1) or not line[cn+1].isdigit()):
      if any([check_for_symbol(j, ln, len(line), total_lines) for  (i, j) in current]):
        valid.append(current)
      current = []

total = sum(int(i) for i,j in [reduce((lambda x,y: (str(x[0]) + str(y[0]), 0)), v) for v in valid])

print(total)
