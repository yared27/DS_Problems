t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    max_wealth = max(a)

    left, right = 0, 10**15
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        new_total = total + mid
        avg = new_total / n
        half_avg = avg / 2

        count = 0
        for w in a:
            if w < half_avg:
                count += 1

        if count > n // 2:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)
