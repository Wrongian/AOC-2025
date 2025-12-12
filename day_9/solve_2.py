# reds_raw = open("input.txt", 'r').read().splitlines()
reds_raw = open("sample.txt", 'r').read().splitlines()

reds = []

for red_raw in reds_raw:
  x, y = tuple(map(int, red_raw.split(",")))
  reds.append((x, y))

n = len(reds)

edges = []
for i in range(1, n):
  edges.append((reds[i - 1], reds[i])) 

# wrap
edges.append((reds[-1], reds[0]))

largest = 0

for i in range(n):
  for j in range(i + 1, n):
    r1_x, r1_y = reds[i]
    r2_x, r2_y = reds[j]

    # make sure r1_x >= r2_x
    if r2_x > r1_x:
      r1_x, r2_x = r2_x, r1_x

    # make sure r1_y >= r2_y
    if r2_y > r1_y:
      r1_y, r2_y = r2_y, r1_y

    is_intercept = False
    for v1, v2 in edges:
      x1, y1 = v1
      x2, y2 = v2
      
      # check horizontal line
      if y1 == y2:
        # if inbetween
        if y1 < r1_y and y1 > r2_y:
          min_x = min(x1, x2)
          max_x = max(x1, x2)
          # overlapping intervals problem
          if max(min_x, r2_x) < min(max_x, r1_x):
            is_intercept = True 
            break
      
      # check vertical line
      if x1 == x2:
        # if inbetween
        if x1 < r1_x and x1 > r2_x:
          min_y = min(y1, y2)
          max_y = max(y1, y2)

          # overlapping intervals problem
          if max(min_y, r2_y) < min(max_y, r1_y):
            is_intercept = True 
            break
      
    if is_intercept:
      continue

    # edge case: rectangle not on any grid tiles but hugging the boundaries
    # use midpoint
    mid_x = (r1_x + r2_x) // 2
    mid_y = (r1_y + r2_y) // 2
    
    # check if rec contains
    # use vert lines
    is_inside = False
    for v1, v2 in edges:
      x1, y1 = v1
      x2, y2 = v2

      if x1 != x2:
        continue

      # make sure y1 > y2
      if y2 > y1:
        y1, y2 = y2, y1
      
      # to the right 
      if x1 > mid_x:
        # check intercept
        if mid_y <= y1 and mid_y >= y2:
          is_inside = not is_inside
    
    if not is_inside:
      continue

    # valid rec
    area = (abs(r1_x - r2_x) + 1) * (abs(r1_y - r2_y) + 1)

    largest = max(largest, area)

print(largest)