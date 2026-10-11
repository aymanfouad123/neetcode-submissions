class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        initial idea: two pointer right off the bat 
        goal is to find the max volume 
        keep a trailing max vol count and update the smaller of the two pointers 
        """
        l, r = 0, len(heights)-1
        maxVol = 0
        
        while l<r:
            volume = min(heights[l],heights[r])*(r-l)  # min because of overflow 
            maxVol = max(volume, maxVol)

            if heights[l] >= heights[r]:
                r -= 1 
            else:
                l += 1 
        
        return maxVol



            

            


