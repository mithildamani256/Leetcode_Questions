import heapq

class MedianFinder(object):

    def __init__(self):
        self.low = []   # max-heap via negatives (lower half)
        self.high = []  # min-heap (upper half)

    def addNum(self, num):
        heapq.heappush(self.low, -num)

        # ensure ordering: max(low) <= min(high)
        if self.high and -self.low[0] > self.high[0]:
            heapq.heappush(self.high, -heapq.heappop(self.low))

        # rebalance sizes: low can have at most 1 more than high
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self):
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0
