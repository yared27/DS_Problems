from bisect import bisect_right
for _ in range(2):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()  # Sort once

    result = [bisect_right(a, bj) for bj in b]
    print(' '.join(map(str, result)))
