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

        # my naive approach -
        """
        result = []

        for idx, ele in enumerate(nums):
            checkVal = target - ele
            # we need to return the current idx with the idx of the valid element
            if checkVal in nums[idx+1:]:
                return [idx, nums.index(checkVal)] # bug on this line because we recount here. 
        
        return result
        """

        # hashmap - O(n)
        """
        result = {}

        for idx, ele in enumerate(nums):
            checkVal = target - ele
            if checkVal in result:
                return [result[checkVal], idx]
            result[ele] = idx
        """

        # two pointer approach - O(nlogn)
        
        # nums = nums.sort() - avoid doing this early on
        # since we loose the original indexing!
        
        # temp = {} - avoid using dict eventhough its easy to store ele with index
        # because same ele vals will loose their original indexing
        # use a list instead!

        temp = []
        for idx, ele in enumerate(nums):
            temp.append([ele,idx])
        temp.sort()

        i, j = 0, len(nums)-1

        # gotta use while 
        while i < j:
            diff = temp[j][0] + temp[i][0]    # make sure to not do "-", we arent doing the target sub 
            if diff == target:
                # return [temp[i][1],temp[j][1]] 
                # this will give errors when theres negative ele vals since the idexing will end up being opposite ie, [a,b] rather than [b,a]
                return [min(temp[i][1], temp[j][1]), max(temp[i][1], temp[j][1])]
            if diff < target:
                i += 1 
            else: 
                j -= 1
            
                


        

        

        

