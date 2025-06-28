class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        pairs=0
        odds=0
        for val,counts in count.items():
            pairs+=counts//2
            odds+=counts%2
        return [pairs,odds]