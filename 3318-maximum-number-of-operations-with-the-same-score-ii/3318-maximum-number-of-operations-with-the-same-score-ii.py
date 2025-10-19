class Solution:
    def maxOperations(self, nums: List[int]) -> int:

        n = len(nums)

        @lru_cache(6000)
        def dp(i: int,j: int,target: int)-> int:

            if j - i < 2: return (j - i == 1 and nums[i]+nums[j]==target)

            return max(1+dp(i+2, j  , target) if nums[i]+nums[i+1] == target else 0,
                       1+dp(i  , j-2, target) if nums[j]+nums[j-1] == target else 0,
                       1+dp(i+1, j-1, target) if nums[i]+nums[j  ] == target else 0)
          
            
        return 1+max(dp(2, n - 1, nums[ 0] + nums[ 1]), 
                     dp(0, n - 3, nums[-1] + nums[-2]), 
                     dp(1, n - 2, nums[ 0] + nums[-1]))