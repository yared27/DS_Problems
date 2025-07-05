class NumArray:

    def __init__(self, nums: List[int]):
        self.nums =nums
    def sumRange(self, left: int, right: int) -> int:
        prefixSum = [0]
        for num in self.nums:
            prefixSum.append(prefixSum[-1]+num)
        return prefixSum[right+1] - prefixSum[left]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)