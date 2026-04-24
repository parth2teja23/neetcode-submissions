class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean, prevHeight):
            if ((r,c) in ocean or
            r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            heights[r][c] < prevHeight):
                return
            ocean.add((r, c))
            dfs(r-1, c, ocean, heights[r][c])
            dfs(r+1, c, ocean, heights[r][c])
            dfs(r, c+1, ocean, heights[r][c])
            dfs(r, c-1, ocean, heights[r][c])

    
        for r in range(ROWS):
            # Pacific (top to bottom):
            dfs(r, 0, pacific, heights[r][0])
            # Atlantic (bottom to top)
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
            
        
        for c in range(COLS):
            #Pacific (Left to right)
            dfs(0, c, pacific, heights[0][c])
            # Atlantic (Right to Left)
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r,c])
        return res 
