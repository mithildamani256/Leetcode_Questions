class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """

        maxProfit = []  # max heap (store negative profits)
        minCapital = [(c, p) for c, p in zip(capital, profits)]

        heapq.heapify(minCapital)

        for _ in range(k):

            # Move all affordable projects into maxProfit
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)

            # No affordable projects left
            if not maxProfit:
                break

            # Take the most profitable affordable project
            w += -heapq.heappop(maxProfit)

        return w