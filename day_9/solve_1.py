reds_raw = open("input.txt", 'r').read().splitlines()
# reds_raw = open("sample.txt", 'r').read().splitlines()

reds = []

for red_raw in reds_raw:
  reds.append(tuple(map(int, red_raw.split(","))))

largest = 0
n = len(reds)

for i in range(n):
  for j in range(i + 1, n):
    r1_x, r1_y = reds[i]
    r2_x, r2_y = reds[j]
  
    area = (abs(r1_x - r2_x) + 1) * (abs(r1_y - r2_y) + 1)

    largest = max(largest, area)

print(largest)
    