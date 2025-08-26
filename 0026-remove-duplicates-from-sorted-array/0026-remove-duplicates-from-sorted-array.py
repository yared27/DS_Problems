class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=collections.Counter(nums)
        k=0
        for n in count:
            nums[k]=n
            k+=1
        return k