intervals = open("input.txt", "r").read()[:-1].split(",")
# intervals = open("sample.txt", "r").read()[:-1].split(",")

total = 0

for interval in intervals:
  left, right = tuple(map(int, interval.split("-")))
  for num in range(left, right + 1):
    num_str = str(num)
    num_len = len(num_str)
    first_half = num_str[:num_len // 2]
    second_half = num_str[num_len // 2:]
    if first_half == second_half:
      total += num 
    
  

print(total)