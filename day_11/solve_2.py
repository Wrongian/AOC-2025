devices = open("input.txt").read().splitlines()
# devices = open("sample.txt").read().splitlines()

adj = {}
for device in devices:
  name, outputs_raw = device.split(": ")

  adj[name] = outputs_raw.split(" ")

# assume acyclic directed graph
num_paths = {}
num_paths[("out", True, True)] = 1
num_paths[("out", False, False)] = 0
num_paths[("out", True, False)] = 0
num_paths[("out", False, True)] = 0
def dfs(node, visit_dac, visit_fft):

  # update
  if node == "dac":
    visit_dac = True
  elif node == "fft":
    visit_fft = True

  key = (node, visit_dac, visit_fft)

  # termination 
  if key in num_paths:
    return num_paths[key]

  # propagation
  # assume every node exists in adj
  total = 0
  for v in adj[node]:
    total += dfs(v, visit_dac, visit_fft)
  
  num_paths[key] = total
  return num_paths[key]

print(dfs("svr", False, False))