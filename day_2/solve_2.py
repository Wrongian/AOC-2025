intervals = open("input.txt", "r").read()[:-1].split(",")
# intervals = open("sample.txt", "r").read()[:-1].split(",")

total = 0

for interval in intervals:
  left, right = tuple(map(int, interval.split("-")))
  for num in range(left, right + 1):
    num_str = str(num)
    num_len = len(num_str)
    for i in range(1,num_len // 2 + 1):
      # cannot be divided equally
      if num_len % i != 0:
        continue

      is_invalid = False
      for j in range(1, num_len // i):
        if num_str[(j - 1) * i: j * i] != num_str[j * i: (j + 1) * i]:
          is_invalid = True
          break
      
      if not is_invalid:
        total += num
        # dont count twice
        break


print(total)