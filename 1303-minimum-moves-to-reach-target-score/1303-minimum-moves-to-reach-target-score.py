class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        move = 0
        while target>1:
            if maxDoubles==0:
                return move+(target-1)
            elif target%2==0:
                target//=2
                maxDoubles-=1
            else:
                target-=1
            move+=1
                  
        return move

            
