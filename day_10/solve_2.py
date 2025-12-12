import re
import numpy as np
from scipy.optimize import milp, LinearConstraint

lines = open("input.txt", 'r').read().splitlines()
# lines = open("sample.txt", 'r').read().splitlines()

total = 0
for line in lines:
  paren_numbers = re.findall(r"\(([\d,]+)\)", line)
  cur_buttons = [list(map(int, group.split(','))) for group in paren_numbers]

  curly_content = re.search(r"\{([^\}]+)\}", line).group(1)
  joltages = list(map(int, curly_content.split(',')))

  jolt_len = len(joltages)
  num_buttons = len(cur_buttons)

  # build matrix
  A = []
  for pos in range(jolt_len):
    row = []
    for button in cur_buttons:
      row.append(1 if pos in button else 0)
    A.append(row)
    
  A = np.array(A)

  # transpose
  A_T = A.T

  B = np.array(joltages)

  # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.milp.html

  # min obj function
  c = np.ones(num_buttons)

  # set up linear eqn
  constraints = LinearConstraint(A, lb=B, ub=B)
  
  # all integers
  is_integer_arr = np.ones(num_buttons) 

  # minimises decision variable x with objective function c, while satisfying constraints
  result = milp(c=c, constraints=constraints, integrality=is_integer_arr)
  
  x_optimal = result.x
  presses = int(np.sum(x_optimal))
  total += presses

print(total)

  


