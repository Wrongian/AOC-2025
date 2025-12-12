lines = open("input.txt", 'r').read().splitlines()
# lines = open("sample.txt", 'r').read().splitlines()

col_len = len(lines) - 1

max_len = 0
for line in lines:
  max_len = max(max_len, len(line))

total = 0
cur_len = 0
trans_nums = ['' for i in range(cur_len)]
op = "+"
for i in range(max_len):
  new_op = lines[-1][i] 
  # flush
  if new_op != " ":
    if op == "+":
      cur = 0
    else:
      cur = 1
    for j in range(cur_len):
      if trans_nums[j].strip() == "":
        continue
      
      if op == "+":
        cur += int(trans_nums[j].strip())
      else:
        cur *= int(trans_nums[j].strip())
    total += cur
    cur_len = 0
    trans_nums = []
  
    op = new_op

  num_str = ""
  for j in range(col_len):
    num_str += lines[j][i]
  cur_len += 1
  trans_nums.append(num_str)


# flush remaining
if op == "+":
    cur = 0
else:
  cur = 1
  
for j in range(cur_len):
  if trans_nums[j].strip() == "":
    continue
  
  if op == "+":
    cur += int(trans_nums[j].strip())
  else:
    cur *= int(trans_nums[j].strip())
total += cur

print(total)