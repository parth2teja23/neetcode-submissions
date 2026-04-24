class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(grid, i , j)
                    count += 1
        return count