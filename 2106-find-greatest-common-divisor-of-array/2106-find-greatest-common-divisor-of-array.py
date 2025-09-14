class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        laregest = max(nums)
        for i in range(smallest, 0, -1):
            if smallest % i == 0 and laregest % i == 0:
                return i
        return 1