class Solution:
    def findLHS(self, nums: List[int]) -> int:
        left = 0
        nums.sort()
        ans=0
        for right in range(len(nums)):
            while nums[right]-nums[left]>1:
                left+=1
            if nums[right]-nums[left]==1:
                ans = max(ans,right-left+1)
         
        return ans

            
