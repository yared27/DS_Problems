# Problem: Given n flowers to pick and m flower types (each with initial happiness a[i] and bonus b[i] per extra flower), choose exactly n flowers to maximize total happiness.
#
# Approach: Sort flower types by descending b[i] (bonus value), try picking each type as the main one, and simulate filling remaining flowers with the best a[i] values using a prefix sum.
#
# Why: You only need to consider top m best a[i] values and simulate placing the current type's flowers last — reducing the search to O(m log m) per test case.

import sys
import bisect

def solve():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        while idx < len(data) and data[idx] == '':
            idx += 1

        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2

        flowers = []
        for _ in range(m):
            a = int(data[idx])
            b = int(data[idx + 1])
            flowers.append((a, b))
            idx += 2

        flowers.sort(reverse=True)
        a_values = [a for a, b in flowers]

        prefix = [0]
        for a in a_values:
            prefix.append(prefix[-1] + a)

        max_happiness = 0

        for i in range(m):
            a_i, b_i = flowers[i]

            # Count how many flowers have 'a' greater than a_i
            pos = bisect.bisect_right(a_values, a_i, lo=0, hi=m)
            cnt = min(n, i)

            rest = n - cnt - 1
            if rest < 0:
                rest = 0

            happiness = prefix[cnt] + a_i + b_i * rest
            max_happiness = max(max_happiness, happiness)

        results.append(max_happiness)

    for res in results:
        print(res)

# Example usage if testing manually:
# solve()
