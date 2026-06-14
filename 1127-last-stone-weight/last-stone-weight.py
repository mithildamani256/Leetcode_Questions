class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        heap = []

        for value in stones:
            heapq.heappush(heap, -value)

        while len(heap) > 1:
            x = - heapq.heappop(heap)
            y = - heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, - (x - y))

        if len(heap) == 1:
            return - heap[0]

        return 0