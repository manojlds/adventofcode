import uuid
from functools import reduce

lines = open("input.txt", "r").read().splitlines()
total_lines = len(lines)
gears = {}
parts = {}

def generate_coords(x,y, xmax, ymax):
  coords = []
  for i in range(max(x-1, 0), min(x+1, xmax) + 1):
    for j in range(max(y-1, 0), min(y+1, ymax) + 1):
      if not (i == x and j == y):
        coords.append((i,j))
  return coords

def find_gear(cn, ln, num_characters, num_lines, part_number):
  for x,y in generate_coords(cn, ln, num_characters-1, num_lines-1):
    if lines[y][x] == "*":
      current = gears.get((x,y), set())
      current.add(part_number)
      gears[(x,y)] = current

for ln, line in enumerate(lines):
  current = []
  for cn,c in enumerate(line):
    if c.isdigit():
      current.append((int(c), cn))
    if current and ((cn == len(line) - 1) or not line[cn+1].isdigit()):
      current_num = reduce((lambda x,y: (str(x[0]) + str(y[0]), 0)), current)
      current_num = current_num[0]
      id = uuid.uuid4()
      parts[id] = int(current_num)
      for i,j in current:
        find_gear(j, ln, len(line), total_lines, id)
      current = []

ratios = []
for g in gears:
  if len(gears[g]) > 1:
    ratio = reduce(lambda x,y: parts[x] * parts[y], gears[g])
    ratios.append(ratio)
    
sum(ratios)
