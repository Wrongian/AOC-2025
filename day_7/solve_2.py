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

memo = {}

def dfs(r, c):
  # termination 
  if r < 0 or c < 0 or r >= m or c >= n:
    # one timeline
    return 1

  if (r, c) in memo: 
    return memo[(r, c)]

  nr = r + 1

  # check splitter
  if (nr, c) in splitters:
    timelines = 0

    for dc in [-1, 1]:
      nc = c + dc
      timelines += dfs(nr, nc)
    
    memo[(r, c)] = timelines

  # move downwards if no splitter
  else:
    timelines = dfs(nr, c)
    memo[(r, c)] = timelines
  
  return memo[(r, c)]


print(dfs(start[0], start[1]))



  



