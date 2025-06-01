class Solution(object):
    def distributeCandies(self, n, limit):
        def comb(n, k):
            if k < 0 or k > n:
                return 0
            res = 1
            for i in range(1, k + 1):
                res = res * (n - i + 1) // i
            return res

        def ways(x):
            return comb(x + 2, 2) if x >= 0 else 0

        l = limit + 1
        return (
            ways(n)
            - 3 * ways(n - l)
            + 3 * ways(n - 2 * l)
            - ways(n - 3 * l)
        )
