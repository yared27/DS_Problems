class Solution:
    def __init__(self):
        self.memo = {0:0, 1:1, 2:1}
    def tribonacci(self, n: int) -> int:
        for i in range(n):
            if i+3 not in self.memo:
                self.memo[i+3] = self.memo[i] + self.memo[i+1] +self.memo[i+2]
        return self.memo[n]
            



