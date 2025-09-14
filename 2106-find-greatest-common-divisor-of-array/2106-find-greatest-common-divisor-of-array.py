class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        laregest = max(nums)
        ans = 0
        for i in range(1, smallest + 1):
            if smallest % i == 0 and laregest % i == 0:
                ans = i
        return ans