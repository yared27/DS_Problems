class Solution:
    def __init__(self):
        self.memo ={}
        
    def dp(self,idx,memo,num):
        if idx>=len(num):
            return 0
        if idx not in memo:
            leave = self.dp(idx+1,memo,num)
            take = num[idx] + self.dp(idx+2,memo,num)
            memo[idx] = max(leave, take)
        return memo[idx]

    def rob(self, nums: List[int]) -> int:
        return self.dp(0,self.memo,nums)


        
        


        