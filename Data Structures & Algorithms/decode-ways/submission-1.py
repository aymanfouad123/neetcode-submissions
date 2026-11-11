class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            # 1. base case checks
            if i == len(s):     # decoded everything 
                return 1
            if s[i] == "0":     # invalid start
                return 0
            
            # 2. check memo
            if i in memo:       
                return memo[i]

            # 3. explore ways 
            # choice 1: take one digit
            res = dfs(i + 1)

            # choice 2: if valid we take two digits
            if i + 1 < len(s) and (
                s[i] == "1" or 
                s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            
            # 4. memoize
            memo[i] = res
            
            return res
        
        return dfs(0)