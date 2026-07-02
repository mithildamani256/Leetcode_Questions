class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hashmap = {}

        for value in nums:
            hashmap[value] = hashmap.get(value, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for value,freq in hashmap.items():
            buckets[freq].append(value)
        
        res = []

        count = k

        for i in range(len(nums), -1, -1):
            for value in buckets[i]:
                res.append(value)

                if len(res) == k:
                    return res


        # hashmap = {}

        # for value in nums:
        #     hashmap[value] = hashmap.get(value, 0) + 1

        # heap = []

        # for value in hashmap:
        #     heap.append((-hashmap[value], value))

        # heapq.heapify(heap)

        # result = []

        # for _ in range(k):
        #     count, value = heapq.heappop(heap)

        #     result.append(value)

        # return result
        