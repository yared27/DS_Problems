class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            indx = abs(num) - 1
            if nums[indx] < 0:
                ans.append(abs(num))
            else:
                nums[indx] = -nums[indx]
        return ans 
