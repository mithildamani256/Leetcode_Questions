class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hashmap = {}
        heap = []

        for value in nums:
            hashmap[value] = hashmap.get(value, 0) + 1
        
        for value in hashmap:
            heapq.heappush(heap, (- hashmap[value], value))

        result = []

        for _ in range(k):
            count, value = heapq.heappop(heap)
            result.append(value)

        return result
        