objs = open("input.txt", 'r').read().split("\n\n")
# objs = open("sample.txt", 'r').read().split("\n\n")


shapes_raw = objs[:-1]

regions_raw = objs[-1]

shape_counts = []
for shape_raw in shapes_raw:
  _, shape_tiles = shape_raw.split(":\n")
  shape = shape_tiles.splitlines()
  count = 0
  # count space in shape
  for r in range(3):
    for c in range(3):
      if shape[r][c] == "#":
        count += 1
  shape_counts.append(count)
  
  
total = 0
for region_raw in regions_raw.splitlines():
  sizes_raw, req_presents_raw = region_raw.split(": ")
  sizes = tuple(map(int, sizes_raw.split("x")))
  req_presents = tuple(map(int ,req_presents_raw.split(" ")))

  have = sizes[0] * sizes[1]

  needed = 0
  for i, num in enumerate(req_presents):
    needed += num * shape_counts[i] 
  
  if needed <= have:
    total += 1

print(total)