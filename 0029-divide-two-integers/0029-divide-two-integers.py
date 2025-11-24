class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
      
       answer = (dividend / divisor)
       if 0 < answer < 2147483648:
            answer = (math.floor(answer))
       elif answer >= 2147483648:
        answer = 2147483647
       else:
        answer = (math.ceil(answer))
       return answer