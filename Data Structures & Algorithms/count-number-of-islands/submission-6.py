class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # approach - dfs w/o set, remarking visited spots
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def dfs(r, c):
            if (r in range(ROWS) and
                c in range(COLS) and
                grid[r][c] == "1"):
                
                # marking visited nodes as "0"
                grid[r][c] = "0"    
                
                for dr, dc in directions:
                    dfs(r + dr, c + dc)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands   

