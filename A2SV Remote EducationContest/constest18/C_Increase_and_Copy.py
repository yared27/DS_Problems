import math
t = int(input())
for _ in range(t):
    n = int(input())
    ans = float('inf')
    for inc in range(0, int(math.sqrt(n)) + 2):
        initial = 1 + inc
        remaining = n - (1 + inc)
        copy_count = 0 if remaining <= 0 else (remaining + initial - 1) // initial
        moves = inc + copy_count
        ans = min(ans, moves)
    print(ans)
