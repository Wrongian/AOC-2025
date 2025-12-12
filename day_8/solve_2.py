from heapq import heappush, heappop

raw_coords = open("input.txt", 'r').read().splitlines()
# raw_coords = open("sample.txt", 'r').read().splitlines()

coords = []
for coord in raw_coords:
  coords.append(tuple(map(int, coord.split(","))))

num_coords = len(coords)

# by index
parent = [i for i in range(num_coords)]
height = [0 for i in range(num_coords)]
size = [1 for i in range(num_coords)]

def union(v1, v2):
  p1, p2 = find(v1), find(v2)
  # cannot union
  if p1 == p2:
    return False
  if height[p1] > height[p2]:
    parent[p2] = p1
    size[p1] += size[p2]
  elif height[p2] > height[p1]:
    parent[p1] = p2
    size[p2] += size[p1]
  else:
    # same height
    parent[p1] = p2
    height[p2] += 1
    size[p2] += size[p1]
  return True

def find(v):
  if parent[v] != v:
    parent[v] = find(parent[v])
  return parent[v]

heap = []
for i in range(num_coords):
  for j in range(i + 1, num_coords):
    x1, y1, z1 = coords[i]
    x2, y2, z2 = coords[j]
    # dont need sqrt since lowest dist
    dist = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2

    # hopefully no ties :3
    heappush(heap, (dist, i, j))

ans = 0
while heap:
  _, i, j = heappop(heap)
  union(i, j)
  if size[find(i)] == num_coords:
    # always from diff circuits
    ans = coords[i][0] * coords[j][0]
    break
  
print(ans)