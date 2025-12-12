file = open("input.txt", 'r')
# file = open("sample.txt", 'r')
rotates = file.readlines()

cur = 50
total = 0

for rotate in rotates:
  dir = rotate[0]
  num = int(rotate[1:])

  if dir == "L":
    cur -= num
  else:
    cur += num
  cur %= 100
  
  if cur == 0:
    total += 1


print(total)
  

