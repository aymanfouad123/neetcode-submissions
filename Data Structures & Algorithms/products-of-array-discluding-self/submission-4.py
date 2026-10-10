class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        initial idea: 
        goal is O(n) time

        0   1   2   3
        1   2   4   6
        
        1   2   8   48  -- a
            0x1     0x1x2x3
        48  48  24  6   -- b
                2x3   
        6   24  48  48
        3   3x2     3x2x1x0    
    
    #   48, 24, 12, 8
        
        result[0] = 48 
        
        for 1,
        result[1] = a[i-1]*b[i+1]

        for 2, 
        result[2] = a[1]*b[3] = 2*6 = 12

        for 3, 
        result[3] = a[2]*b[4] = 8

        """

        # above approach 
        """
        fprod = []
        count = 1
        for x in range(len(nums)):
            count *= nums[x]
            fprod.append(count)

        rprod = []
        count = 1 
        for i in range(len(nums)-1, -1,-1):
            count *= nums[i]
            rprod.append(count)
        rprod = rprod[::-1]

        result = [0 for _ in range(len(nums))]
        result[0] = rprod[1]
        result[len(nums)-1] = fprod[-2]

        for r in range(1, len(nums)-1):
            result[r] = fprod[r-1]*rprod[r+1]
        
        return result
        
        although the above is O(n) time 
        theres a more memory efficient solution where we dont have to create a prefix and postfix array and can do the same operations on the original nums
        """

        result = [1]*len(nums)

        prefix = 1
        
        for i in range(len(nums)):
            result[i] = prefix
            prefix*=nums[i]
        
        postfix = 1
        for x in range(len(nums)-1,-1,-1):
            result[x] *= postfix
            postfix *= nums[x]

        # here we used result for both the passes, hence memory efficient
        return result




        
            




