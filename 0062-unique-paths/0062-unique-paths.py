class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def uniquePath(coord):
            row, col = coord
            if (row,col)==(m-1,n-1):
                return 1
            ways = 0
            if col+1<n:
                ways += uniquePath((row,col+1))
            if row+1<m:
                ways += uniquePath((row+1, col))
            return ways
        return uniquePath((0,0))
            



        
