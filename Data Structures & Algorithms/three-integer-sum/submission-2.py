class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        remember: two pointer approach works only on sorted arrays

        method 1 - hashmaps; O(n^2) time but O(n) space
        method 2 - pointers; O(n^2) time but O(1) space
        """
        
        # method 1 
        nums.sort()

        count = defaultdict(int)
        for ele in nums:
            count[ele] += 1
        
        result = []

        for i in range(len(nums)):
            # reduce freq to avoid duplicates
            count[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue    # same values will have the same combinations
            
            for x in range(i+1, len(nums)):
                count[nums[x]] -= 1 
                if x-1> i and nums[x] == nums[x-1]:
                    continue    # first ele check + dup check
                target = - (nums[x] + nums[i])  # calculating the value we're looking for
                if count[target] > 0:
                    # since the value is present we can simply use target 
                    result.append([nums[i], nums[x], target])
            
            for j in range(i+1, len(nums)):
                count[nums[j]] += 1 
        return result 


            
