class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        # now the max pali length will be len(s)
        # my initial idea is to go from 0 to len values,
        and opt for a sliding window like approach
        
        now the min window is 3, where for 1 or 2 as min
        length we just return empty since it can be a pali
        '''

        result = [""]

        for i in range(1, len(s)+1):
            # here i is the sliding window size

            # we will probably need another loop to move the
            # window

            # purpose of loop 1 = get a substring length 
            
            # so right now lets assume i = 3
            for x in range(len(s)):
                # purpose of loop 2 is to have the sliding
                # window logic given the i above 
                if x+i <= len(s):
                    subarr = s[x:x+i]
                    checkpali = self.isPali(subarr)
                    if checkpali:

                        result.append(subarr)
                else: break

        return max(result, key=len)








    def isPali(self, arr):
        return arr == arr[::-1]