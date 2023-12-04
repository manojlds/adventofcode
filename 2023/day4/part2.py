import re

with open("input.txt", "r") as f:
  lines = f.read().splitlines()

num_cards = len(lines)  

def process_numbers(l):
  return set(s.strip() for s in l.split(" ") if s!="")
cards = {}
for line in lines:
  card_number_match = re.match("Card\s+(\d+): ", line)
  card_number = int(card_number_match[1])
  line = line.replace(card_number_match[0], "")
  [winning, present] = [s.strip() for s in line.split("|")]

  winning_numbers = process_numbers(winning)
  present_numbers = process_numbers(present)

  num_match = len(winning_numbers.intersection(present_numbers))
  
  current_times = cards.get(card_number, 0)
  current_times += 1
  cards[card_number] = current_times
  for i in range(current_times):
    for n in range(card_number + 1, card_number + num_match + 1):
      if n > num_cards:
        break
      current = cards.get(n, 0)
      cards[n] = current + 1

sum(cards.values())
