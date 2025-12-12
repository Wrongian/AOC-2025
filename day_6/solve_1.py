lines = open("input.txt", 'r').read().strip().splitlines()
# lines = open("sample.txt", 'r').read().strip().splitlines()

numbers = [list(map(int, line.split())) for line in lines[:-1]]

ops = lines[-1].split()

total = 0
for i, op in enumerate(ops):
  if op == '+':
    cur = 0
  else:
    cur = 1
  for arr in numbers:
    if op == "+":
      cur += arr[i]
    else:
      cur *= arr[i]
  total += cur

print(total)

