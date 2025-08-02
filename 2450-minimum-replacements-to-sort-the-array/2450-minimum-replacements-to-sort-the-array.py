class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        maxAllowed = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > maxAllowed:
                parts = ceil(nums[i] / maxAllowed)
                operations += parts - 1
                maxAllowed = nums[i] // parts
            else:
                maxAllowed = nums[i]

        return operations
