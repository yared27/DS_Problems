class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        n= len(colors)
        i=1
        while i<n:
            if colors[i]==colors[i-1] :
                if neededTime[i] < neededTime[i-1]:
                    ans += neededTime[i]
                    neededTime[i]=neededTime[i-1]
                else:
                    ans += neededTime[i-1]
            i+=1
        return ans