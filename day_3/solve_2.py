banks = list(map(lambda x : x[:-1], open("input.txt", 'r').readlines()))
# banks = list(map(lambda x : x[:-1], open("sample.txt", 'r').readlines()))

total = 0
for bank in banks:
  num = 0
  max_index = -1
  for k in range(11, -1, -1):
    # max left
    max_digit = int(bank[max_index + 1])
    max_i = max_index + 1
    for i in range(max_index + 1, len(bank) - k):
      if int(bank[i]) > max_digit:
        max_digit = int(bank[i])
        max_i = i
    
    max_index = max_i 
    num *= 10
    num += max_digit
      
  total += num

print(total)




  

