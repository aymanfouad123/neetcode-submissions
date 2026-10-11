class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # method 2 - two pointers 
        result = []

        nums.sort()

        for i in range(len(nums)):
            # here we treat i as the target 
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            l, r = i+1, len(nums)-1 
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])

                    # since there can still be other l, r pairs 
                    l += 1 
                    r -= 1 
                    while l < r and nums[l] == nums[l-1]:
                        # skipping repeating l
                        l += 1 
        
        return result 


        