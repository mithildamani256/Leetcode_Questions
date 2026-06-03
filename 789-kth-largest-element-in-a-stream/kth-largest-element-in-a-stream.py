class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

        self.heap = nums
        self.k = k

        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)