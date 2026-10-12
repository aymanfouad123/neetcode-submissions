class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        initial idea:
        keep increasing window till max diff - window should be lower than k
        """
        
        count = defaultdict(int)
        l = 0
        maxVal = 0

        for r in range(len(s)):
            count[s[r]] += 1
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1 
                l += 1 
            
            maxVal = max(maxVal, r-l+1)
        
        return maxVal
                

















