class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_birr = 0
        ten_birr = 0
        twenty_birr = 0
        for birr in bills:
            if birr==5:
                five_birr+=1
            elif birr==10:
                if five_birr>0:
                    five_birr-=1
                    ten_birr+=1
                else:
                    return False
            else:
                if ten_birr>0 and five_birr>0:
                    ten_birr-=1
                    five_birr-=1
                elif five_birr>=3:
                    five_birr-=3
                else:
                    return False
        return True