t = int(input())
for _ in range(t):
    n = int(input())
    m = (n - 1) // 2
    total_moves = 8 * m * (m + 1) * (2 * m + 1) // 6
    print(total_moves)
