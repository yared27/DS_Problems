class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        pairs=0
        odds=0
        for val,counts in count.items():
            if counts%2==0:
                pairs+=(counts)//2
            else:
                odds+=1
                pairs+=(counts-1)//2
        return [pairs,odds]