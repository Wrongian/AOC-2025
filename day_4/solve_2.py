from collections import deque

grid = open("input.txt", 'r').read().split("\n")[:-1]
# grid = open("sample.txt", 'r').read().split("\n")[:-1]

m = len(grid)
n = len(grid[0])


papers = set()
for r, row in enumerate(grid):
  for c, ele in enumerate(row):
    if ele == "@":
      papers.add((r, c))

removed = 0

q = deque(list(papers))

while q:
  r,c = q.popleft()

  # outdated
  if (r, c) not in papers:
    continue

  adj = 0
  to_check = []

  # check
  for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
    nr, nc = r + dr, c + dc
    if nr < 0 or nc < 0 or nr >= m or nc >= n:
      continue
      
    if (nr, nc) in papers:
      adj += 1
      to_check.append((nr, nc))

  if adj < 4:
    papers.remove((r, c))
    removed += 1
    for (nr, nc) in to_check:
      q.append((nr, nc))


print(removed) 