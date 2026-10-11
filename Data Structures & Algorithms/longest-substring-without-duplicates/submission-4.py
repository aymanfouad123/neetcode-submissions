class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # optimal sliding window approach - i.e, not relying on incremental removes

        latestChar = {}

        l = 0
        maxVal = 0

        for r in range(len(s)):
            if s[r] in latestChar:
                l = max(latestChar[s[r]]+1, l)
                """
                s="abcbcbb"
                so when we encounter an element b when repeated 
                we dont need to do a repeated remove
                but we can use the latest index of b and update l 
                but lets say the older reference is outside the window i.e, we previously did a jump and l is bigger than the original b reference

                we can use the max operator to avoid backtracking the value of l
                """
            
            latestChar[s[r]] = r
            maxVal = max(maxVal, r-l+1)
        
        return maxVal



