class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        def dfs(row, col):
            board[row][col] = 'S'  
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if inbound(new_row, new_col) and board[new_row][new_col] == 'O':
                    dfs(new_row, new_col)
        
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m - 1][j] == 'O':
                dfs(m - 1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
