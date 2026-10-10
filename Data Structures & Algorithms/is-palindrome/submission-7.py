class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        to get O(n) time and O(1) space we can do two pointers 

        we can also do a reverse string check using s[::-1] which will be linear time but not constant space. 
        """

        i, j = 0, len(s)-1 

        while i<j:
            while i<j and not (s[i].isalnum()):
                i+=1 
            while j>i and not (s[j].isalnum()):
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            i += 1 
            j -= 1
        
        return True