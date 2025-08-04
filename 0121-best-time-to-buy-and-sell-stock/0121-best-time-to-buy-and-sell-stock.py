class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        j = 1
        maxProfit = 0
        while j<len(prices) and i < len(prices):
            if prices[i]<prices[j]:
                maxProfit = max(maxProfit, prices[j] - prices[i])
            else:
                i=j
            j+=1
        return maxProfit




