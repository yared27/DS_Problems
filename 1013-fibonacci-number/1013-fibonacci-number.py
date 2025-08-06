class Solution:
    # def __init__(self):
    #     self.memo = {0:0, 1:1}
    def fib(self, n: int) -> int:
        # if n not in self.memo:
        #     self.memo[n] = self.fib(n-1) + self.fib(n-2)
        
        # return self.memo[n]
        ans = [0,1]
        for i in range(2,n+1):
            ans.append(ans[i-1]+ans[i-2])
        return ans[n]
       