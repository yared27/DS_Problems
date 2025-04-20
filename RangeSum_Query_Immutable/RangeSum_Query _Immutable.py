
nums =list(map(int, input().split(',')))
left =int(input("Enter the left start"))
right = int(input("Enter the right"))
class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

# Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)
param_1 = obj.sumRange(left,right)
print(param_1)