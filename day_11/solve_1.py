devices = open("input.txt").read().splitlines()
# devices = open("sample.txt").read().splitlines()

adj = {}
for device in devices:
  name, outputs_raw = device.split(": ")

  adj[name] = outputs_raw.split(" ")

# assume acyclic directed graph
num_paths = {}
num_paths["out"] = 1
def dfs(node):
  # termination 
  if node in num_paths:
    return num_paths[node]
  
  # propagation
  # assume every node exists in adj
  total = 0
  for v in adj[node]:
    total += dfs(v)
  
  num_paths[node] = total
  return num_paths[node]

print(dfs("you"))

