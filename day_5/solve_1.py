ranges_raw, ids_raw = open("input.txt", "r").read().split("\n\n")
# ranges_raw, ids_raw = open("sample.txt", "r").read().split("\n\n")

# 0 is start, 2 is end, 1 is ingre
arr = []

for ran in ranges_raw.split("\n"):
  start, end = ran.split("-")
  arr.append((int(start), 0))
  arr.append((int(end), 2))


for id in ids_raw.split("\n")[:-1]:
  arr.append((int(id), 1))

arr.sort()

cur = 0
fresh = 0
for num, t in arr:
  if t == 0:
    cur += 1
  elif t == 2:
    cur -= 1
  else:
    if cur != 0:
      fresh += 1

print(fresh)
    
