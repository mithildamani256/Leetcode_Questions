class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # # max_diff = 0

        # # for i in range(len(prices)):
        # #     val = prices[i]
        # #     for j in range(i+1, len(prices)):
        # #         stck = prices[j]
        # #         if (stck - val > max_diff):
        # #             max_diff = stck-val

        
        # # return max_diff

        # max_profit = 0

        # buy = prices[0]

        # for stock in prices[1:]:
        #     if stock > buy:
        #         max_profit = max(stock-buy, max_profit)
        #     else:
        #         buy = stock
        
        # return max_profit

        # n = len(prices)

        # max_value = 0

        # for i in range(n):
        #     for j in range(i+1,n):
        #         if prices[j] - prices[i] > max_value:
        #             max_value = prices[j] - prices[i]


        # return max_value

#         The idea of Kadane’s algorithm is to traverse over the array from left to right and for each element,
#  find the maximum sum ending at that element. The result will be the maximum of all these values. 

        max_profit = 0
        min_value = prices[0]

        for price in prices:
            if price - min_value > max_profit:
                max_profit = price - min_value

            if price < min_value:
                min_value = price

        
        return max_profit




