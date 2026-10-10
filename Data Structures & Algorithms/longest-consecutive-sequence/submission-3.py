class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        goal: do this in O(n)
        so we need to figure out a linear pass solution

        note: sets have O(1) time lookups!

        so if for an element num, 
        if num+1 is in nums - where the lookup is O(1)
        then we can keep that loop going and keep a rolling store of the longest sequence

        rather than needing to do that for each element
        we can do the iterations on numbers that dont have a previous value, 
        since then it would signify that the element is the start of a sequence
        """
        
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num-1) not in numSet:
                # start of a potential sequence 
                length = 1
                while (num+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

