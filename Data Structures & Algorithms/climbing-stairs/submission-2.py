class Solution:
    def climbStairs(self, n: int) -> int:
        # dp - top down
        memo = {0: 1, 1: 1}

        def dfs(step):
            if step in memo: return memo[step]

            memo[step] = dfs(step - 1) + dfs(step - 2)
            
            return memo[step]

        return dfs(n)