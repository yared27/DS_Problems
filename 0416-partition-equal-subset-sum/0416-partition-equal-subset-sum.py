class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2!=0:
            return False
        half = sum(nums)//2
        memo = {}
        def dp(i, currentSum):
            if currentSum == half:
                return True
            
            elif i>=len(nums)-1 or currentSum>half:
                return False
            elif (i, currentSum) not in memo:
                memo[(i, currentSum)] = dp(i+1,currentSum + nums[i]) or dp(i+1, currentSum)
            return memo[(i,currentSum)]
        return dp(0,0)  


    