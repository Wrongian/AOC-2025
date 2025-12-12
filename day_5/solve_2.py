ranges_raw, ids_raw = open("input.txt", "r").read().split("\n\n")
# ranges_raw, ids_raw = open("sample.txt", "r").read().split("\n\n")

# 0 is start, 1 is the end
arr = []

for ran in ranges_raw.split("\n"):
  start, end = ran.split("-")
  arr.append((int(start), 0))
  arr.append((int(end), 1))


arr.sort()

cur = 0
fresh = 0
start = None
for num, t in arr:
  if t == 0:
    cur += 1
    if start == None:
      start = num
  else:
    cur -= 1
    if cur == 0:
      fresh += num - start + 1
      start = None

print(fresh)
    
