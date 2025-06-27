class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxWeight = sum(weights)
        minWeight= max(weights)

        def bs(capacity):
            current_day = 0
            sum=0
            for i in weights:
                if sum+i <= capacity:
                    sum+=i
                else:
                    sum=i
                    current_day+=1
            current_day+=1
            return current_day<=days
        

        while minWeight<=maxWeight:
            mid=(minWeight+maxWeight)//2
            if bs(mid):
                maxWeight=mid-1
            else:
                minWeight=mid+1
        return minWeight






