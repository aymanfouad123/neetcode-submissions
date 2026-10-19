class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bfs
        ROWS, COLS = len(heights), len(heights[0])
        
        pacific = deque()
        atlantic = deque()

        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))
        
        def bfs(queue):
            visited = set(queue)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                r, c = queue.popleft()
                for r_off, c_off in directions:
                    nr, nc = r + r_off, c + c_off
                    if (nr in range(ROWS) and
                        nc in range(COLS) and 
                        heights[nr][nc] >= heights[r][c] and 
                        (nr, nc) not in visited):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            return visited

        pSeen = bfs(pacific)
        aSeen = bfs(atlantic)

        return list(pSeen.intersection(aSeen))



