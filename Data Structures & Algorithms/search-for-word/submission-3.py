class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLen, colLen = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            # if we found the word
            if i == len(word): return True

            if (min(r, c) < 0 or
                r >= rowLen or c >= colLen or
                word[i] != board[r][c] or
                (r,c) in path):
                # above we checked for, 
                # bounds, 
                # adj valid char, and 
                # visited combination
                return False
            
            # i.e, we found the char we need
            path.add((r,c))

            # continue dfs on neighbors
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            path.remove((r, c)) # backtrack
            return res
        
        for r in range(rowLen):
            for c in range(colLen):
                if dfs(r, c, 0):
                    return True
        return False