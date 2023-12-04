import re

with open("input.txt", "r") as f:
  lines = f.read().splitlines()

def process_numbers(l):
  return set(s.strip() for s in l.split(" ") if s!="")
scores = []
for line in lines:
  card_number_match = re.match("Card\s+(\d+): ", line)
  line = line.replace(card_number_match[0], "")
  [winning, present] = [s.strip() for s in line.split("|")]

  winning_numbers = process_numbers(winning)
  present_numbers = process_numbers(present)

  num_match = len(winning_numbers.intersection(present_numbers))
  score = pow(2, num_match -1) if num_match > 0 else 0
  scores.append(score)

sum(scores)
