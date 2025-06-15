from collections import defaultdict

n, m = map(int, input().split())

cats = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1  
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * n
stack = [(0, 0)]  
result = 0

while stack:
    node, consecutive = stack.pop()
    visited[node] = True

    if cats[node] == 1:
        consecutive += 1
    else:
        consecutive = 0

    if consecutive > m:
        continue

    is_leaf = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            is_leaf = False
            stack.append((neighbor, consecutive))

    if is_leaf:
        result += 1

print(result)









# graph = {
#     0: [1, 2],
#     1: [0, 3],
#     2: [0],
#     3: [1]
# }
