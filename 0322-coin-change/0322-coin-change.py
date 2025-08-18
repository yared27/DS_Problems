class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        def dp(rem):
            
            if rem == 0:
                return 0
            if rem<0:
                return float("inf")
            if rem in memo:
                return memo[rem]
            
            ans = float("inf")

            for c in coins:
                ans = min(ans, 1+dp(rem-c))
            
            memo[rem] = ans
            return ans

        res = dp(amount)

        return -1 if res == float("inf") else res
            
        

        
