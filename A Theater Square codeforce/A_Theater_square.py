import math
n, m, a = map(int, input().split())

countw = math.ceil(n/a)
cunth=math.ceil(m/a)

print(countw*cunth)