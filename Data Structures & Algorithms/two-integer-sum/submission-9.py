class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        initial idea: go through the list, subtract target from the list values and see if its present inside. 
        we need to return indexes. 
        search the sliced list to avoid recounting the same element

        approaches: 
        1. usual brute force using two loops O(n^2)
        2. sorted list and two pointers O(nlogn)
        3. hashmaps O(n)
        4. my approach below is O(n^2)
        """

        """
        naive approach -

        result = []

        for idx, ele in enumerate(nums):
            checkVal = target - ele
            # we need to return the current idx with the idx of the valid element
            if checkVal in nums[idx+1:]:
                return [idx, nums.index(checkVal)] # bug on this line because we recount here. 
        
        return result
        """

        #hashmap - O(n)
        result = {}

        for idx, ele in enumerate(nums):
            checkVal = target - ele
            if checkVal in result:
                return [result[checkVal], idx]
            result[ele] = idx

        

