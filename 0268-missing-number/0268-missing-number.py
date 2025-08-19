class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = len(nums)

        for i in range(maxNum+1):
            if i not in nums:
                return i

        