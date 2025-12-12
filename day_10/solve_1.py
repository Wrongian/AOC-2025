import re

lines = open("input.txt", 'r').read().splitlines()
# lines = open("sample.txt", 'r').read().splitlines()


total = 0
for line in lines:
  bracket_content = re.search(r"\[([^\]]+)\]", line).group(1)
  target = 0
  for i, c in enumerate(bracket_content):
    if c == "#":
      target |= (1 << i)

  paren_numbers = re.findall(r"\(([\d,]+)\)", line)
  cur_buttons = [list(map(int, group.split(','))) for group in paren_numbers]
  button_arr = []
  for cur_button in cur_buttons:
    button = 0
    for idx in cur_button:
      button |= (1 << idx)
    button_arr.append(button)
  
  # generate all 2^n subsets (starting from the lowest)
  # le power set problem
  # I assume dont skip empty (so can get 0)
  # assume its possible as well for all machines
  min_subset_len = float("inf")
  for mask in range(1 << len(button_arr)):
    subset = []
    for i in range(len(button_arr)):
      if mask & (1 << i):
        subset.append(button_arr[i])

    # xor all numbers in the subset
    cur_num = 0
    for num in subset:
      cur_num ^= num

    if cur_num == target:
      min_subset_len = min(min_subset_len, len(subset))
  
  total += min_subset_len

print(total)

  


