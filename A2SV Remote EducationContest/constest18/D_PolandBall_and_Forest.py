n = int(input())
p = list(map(int, input().split()))

parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[x_root] = y_root

for i in range(n):
    union(i, p[i] - 1)

roots = set(find(i) for i in range(n))
print(len(roots))
