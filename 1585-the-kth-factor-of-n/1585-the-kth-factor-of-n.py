class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        x = 0
        for i in range(1,n+1):
            if n%i == 0:
                x += 1
                if x == k:
                    return i
        return -1