t = int(input())
result = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)

    max_index = a.index(max(a))

    def check(x):
        threshold_numerator = total + x
        count = 0
        for i in range(n):
            val = a[i]
            if i == max_index:
                val += x
            if val * 2 * n < threshold_numerator:
                count += 1
        return count * 2 > n  # more than half discontent

    if check(0):
        result.append(0)
        continue

    if not check(10**15):
        result.append(-1)
        continue

    left, right = 1, 10**15
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    result.append(answer)

for res in result:
    print(res)
