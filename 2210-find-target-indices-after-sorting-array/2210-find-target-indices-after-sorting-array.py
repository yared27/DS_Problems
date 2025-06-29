class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = bisect_left(nums,target)
        right = bisect_right(nums,target)
        print(left)
        print(right)
        return list(range(left,right))