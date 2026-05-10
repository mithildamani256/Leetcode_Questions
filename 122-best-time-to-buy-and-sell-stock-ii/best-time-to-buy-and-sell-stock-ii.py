class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices == []:
            return 0

        buy_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                current_profit = prices[i] - buy_price
                profit += current_profit

                buy_price = prices[i]
        
        return profit
        
