banks = list(map(lambda x : x[:-1], open("input.txt", 'r').readlines()))
# banks = list(map(lambda x : x[:-1], open("sample.txt", 'r').readlines()))

total = 0
for bank in banks:
  # max left
  max_left = int(bank[0])
  max_i = 0
  for i in range(len(bank) - 1):
    if int(bank[i]) > max_left:
      max_left = int(bank[i])
      max_i = i
    
  max_right = int(bank[-1])
  max_j = len(bank) - 1
  for j in range(max_i + 1, len(bank)):
    if int(bank[j]) > max_right:
      max_j = j
      max_right = int(bank[j])
    
  total += max_left * 10 + max_right 

print(total)




  

