grid = open("input.txt", 'r').read().split("\n")[:-1]
# grid = open("sample.txt", 'r').read().split("\n")[:-1]


m = len(grid)
n = len(grid[0])
total = 0
for r, row in enumerate(grid):
  for c, ele in enumerate(row):
    if ele == "@":
      adj = 0
      # check
      for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        nr, nc = r + dr, c + dc
        if nr < 0 or nc < 0 or nr >= m or nc >= n:
          continue
          
        if grid[nr][nc] == "@":
          adj += 1

      if adj < 4:
        total += 1

print(total)
      
        