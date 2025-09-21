class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        count = Counter(nums)
        for key, value in count.items():
            if value == 2:
                ans.append(key)
        return ans
