class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        

        min_value = prices[0]
        total_profit = 0

        for price in prices:            
            if price - min_value > 0:
                total_profit += price - min_value
                
            min_value = price


        return total_profit
        