class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        initial idea: similar to pillar volume, so two pointer approach 
        goal maximize buy low sell high 
        we only need to find the lowest buy and then can check the higher profits from there. 
        """

        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[r] < prices[l]:   # stock cheaper the next day
                l = r
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            r += 1 

        return maxProfit 

             
            

            