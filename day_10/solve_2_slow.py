import re

lines = open("input.txt", 'r').read().splitlines()
# lines = open("sample.txt", 'r').read().splitlines()

total = 0
for line in lines:
  paren_numbers = re.findall(r"\(([\d,]+)\)", line)
  cur_buttons = [list(map(int, group.split(','))) for group in paren_numbers]

  curly_content = re.search(r"\{([^\}]+)\}", line).group(1)
  joltages = list(map(int, curly_content.split(',')))

  jolt_len = len(joltages)

  memo = {}
  # dfs (iterate through all, find optimal)
  def dfs(cur_jolts):
    # termination
    is_overexceed = False
    is_matches = True
    for i in range(jolt_len):
      if cur_jolts[i] > joltages[i]:
        is_overexceed = True
      
      if cur_jolts[i] != joltages[i]:
        is_matches = False

    if is_overexceed: 
      # signal to not take this
      return float("inf")
    
    # 0th step
    if is_matches:
      return 0 
    
    key = tuple(cur_jolts)
    if key in memo:
      return memo[key]
    
    # propagation
    min_presses = float("inf")
    # iterate through all actions
    for button in cur_buttons:
      # increment
      for idx in button: 
        cur_jolts[idx] += 1
      
      # add 1 for the new press
      min_presses = min(min_presses, dfs(cur_jolts) + 1)
      
      # decrement for next
      for idx in button: 
        cur_jolts[idx] -= 1
    
    memo[key] = min_presses
    return memo[key]
  
  total += dfs([0 for i in range(jolt_len)])

print(total)

  


