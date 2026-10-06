class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        initial idea: go for a sliding window approach.
        one loop decides how big the window is, and another 
        moves it.
        check each substring against its reverse, then keep
        the longest.
        '''
        result = [""]

        for i in range(1, len(s) + 1):
            for x in range(len(s)):
                if x + i <= len(s):
                    subarr = s[x:x+i]
                    checkpali = self.isPali(subarr)
                    if checkpali:
                        result.append(subarr)
                else:
                    break

        return max(result, key=len)


    def isPali(self, arr):
        return arr == arr[::-1]