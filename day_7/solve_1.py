from collections import deque

grid = open("input.txt", 'r').read().splitlines()
# grid = open("sample.txt", 'r').read().splitlines()

m = len(grid)
n = len(grid[0])

splitters = set()
start = None

for r, row in enumerate(grid):
  for c, ele in enumerate(row):
    if ele == "S":
      start = (r, c)
    elif ele == "^":
      splitters.add((r, c))

q = deque([start])

splits = 0
visited = set()
while q:
  r, c = q.popleft()


  if (r, c) in visited:
    continue
  visited.add((r, c))

  nr = r + 1

  # check bounds
  if nr < 0 or nr >= m:
    continue
  
  # check splitter
  if (nr, c) in splitters:

    for dc in [-1, 1]:
      nc = c + dc

      if nc < 0 or nc >= n:
        continue

      q.append((nr, nc))
    splits += 1
  # move downwards if no splitter
  else:
    q.append((nr, c))


print(splits)
    

  

