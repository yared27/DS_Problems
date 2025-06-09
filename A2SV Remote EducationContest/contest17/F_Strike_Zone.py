import sys
input = sys.stdin.read

def solve():
    from bisect import bisect_left, bisect_right
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        k = int(data[idx + 2])
        idx += 3
        h = list(map(int, data[idx:idx + n]))
        idx += n
        x = list(map(int, data[idx:idx + n]))
        idx += n

        def can_defeat_k_enemies(T):
            intervals = []
            for i in range(n):
                max_d = m - (h[i] + T - 1) // T
                if max_d < 0:
                    continue
                l = x[i] - max_d
                r = x[i] + max_d
                intervals.append((l, r))

            # Sweep line: compress coordinates
            points = []
            for l, r in intervals:
                points.append(l)
                points.append(r + 1)
            points = sorted(set(points))
            idx_map = {v: i for i, v in enumerate(points)}

            line = [0] * (len(points) + 2)
            for l, r in intervals:
                line[idx_map[l]] += 1
                line[idx_map[r + 1]] -= 1 if r + 1 in idx_map else 0

            curr = 0
            for v in line:
                curr += v
                if curr >= k:
                    return True
            return False

        # Binary search for minimum number of attacks
        lo, hi = 1, max(h)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_defeat_k_enemies(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        results.append(str(ans))

    print("\n".join(results))

solve()
