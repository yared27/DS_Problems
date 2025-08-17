class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo ={}
        def backtracking(i,currentSum):
            
            if i >= len(nums):
                return 1 if currentSum == target else 0           
            if (i, currentSum) not in memo:
                memo[(i,currentSum)] = backtracking(i+1, currentSum-nums[i]) + backtracking(i+1,currentSum+nums[i])
            return memo[(i, currentSum)]
        return backtracking(0,0)




