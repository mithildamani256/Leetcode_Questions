class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0
        buy_day = 0

        for i in range(1, len(prices)):
            if prices[i] - prices[buy_day] > max_profit:
                max_profit = prices[i] - prices[buy_day]
            
            if prices[i] < prices[buy_day]:
                buy_day = i

        return max_profit



        