file = open("input.txt", 'r')
# file = open("sample.txt", 'r')
rotates = file.readlines()

cur = 50
total = 0

for rotate in rotates:
  prev_cur = cur
  dir = rotate[0]
  num = int(rotate[1:])

  if dir == "L":
    cur -= num
  else:
    cur += num

  if cur <= 0:
    total += ((-cur) // 100) + 1
  else:
    total += cur // 100
 
  # edge cases, 0 -> negative
  if prev_cur == 0 and cur < 0:
    total -= 1
  

  cur %= 100

  

print(total)
  

