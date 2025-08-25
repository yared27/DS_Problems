class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for i in range(len(nums)):
            missing^= i+1^(nums[i])
        return missing