class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n,m = len(maze),len(maze[0])
        q = deque([entrance])
        maze[entrance[0]][entrance[1]] = "+"
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        height = 0
        def isBoarder(i,j):
            return (i==0 or i==n-1) or (j==0 or j==m-1) 
        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                for nr, nc in directions:
                    new_row = nr+x
                    new_col = nc+y
                    if 0<=new_row <n and 0<=new_col<m and maze[new_row][new_col]=='.':
                        maze[new_row][new_col]="+"
                        if isBoarder(new_row,new_col):
                            return height+1
                        q.append([new_row,new_col])
            height+=1
        return -1


                        




