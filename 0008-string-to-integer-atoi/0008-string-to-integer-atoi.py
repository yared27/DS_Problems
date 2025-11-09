class Solution:
    def myAtoi(self, s: str) -> int:
        multiply_by = 1
        res_int = 0
        
        if s is "":
            return 0
        
        if len(s) > 1:
            if s[0] is '+' and s[1] is '-':
                return 0
            elif s[1] is '+' and s[0] is '-':
                return 0
        
        temp_str = s.strip()
        for i,char in enumerate(temp_str):
            if char is '-' and i is 0 :
                multiply_by = -1
                continue
            elif char is '+' and i is 0 :
                multiply_by = 1
                continue
            
            if char >= '0' and char <= '9':
                res_int = res_int*10 + int(char)
            else:
                break
                 
            if res_int * multiply_by  > pow(2, 31) - 1:
                return pow(2, 31) - 1
            
            if res_int * multiply_by < -pow(2, 31) :
                return -pow(2, 31)
            
        return res_int * multiply_by
        