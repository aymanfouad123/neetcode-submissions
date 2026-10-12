class Solution:
    def minWindow(self, s: str, t: str) -> str:
        idxCount = {}

        tCheck = defaultdict(int)
        for ele in t:
            tCheck[ele] += 1

        sCheck = defaultdict(int)
        have, need = 0, len(tCheck)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            sCheck[s[r]] += 1 

            if s[r] in tCheck and sCheck[s[r]] == tCheck[s[r]]:
                have += 1 
            
            while have == need:
                # i.e, we've found our initial window
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # now we can try to shrink from l
                sCheck[s[l]] -= 1
                if s[l] in tCheck and sCheck[s[l]] < tCheck[s[l]]:
                    have -= 1
                l += 1 
        
        l, r = res  # updating if window found
        return s[l:r+1] if resLen != float("infinity") else ""
            



            


