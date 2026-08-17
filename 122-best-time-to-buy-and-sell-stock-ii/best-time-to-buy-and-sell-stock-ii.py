class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        total = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            price = prices[i]

            if price <= buy:
                buy = price
            else:
                total += price - buy
                buy = price

        return total 