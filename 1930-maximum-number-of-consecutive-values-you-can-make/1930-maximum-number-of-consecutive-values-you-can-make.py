class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        maxConstructible = 0
        for coin in coins:
            if coin>maxConstructible+1:
                break
            print(maxConstructible)
            maxConstructible+=coin
        return maxConstructible + 1
           