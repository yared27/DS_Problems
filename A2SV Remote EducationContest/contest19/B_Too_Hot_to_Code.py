t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort()
    
    max_len = 1
    left = 0

    for right in range(1, n):
        if a[right] - a[right - 1] <= k:
            pass
        else:
            left = right
        
        max_len = max(max_len, right - left + 1)

    print(n - max_len)
