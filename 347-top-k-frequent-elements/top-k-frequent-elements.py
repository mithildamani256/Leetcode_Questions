class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = [[] for i in range(len(nums) + 1)]

        hashmap = {}
        res = []

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1

        print(hashmap)

        for value in hashmap:
            count = hashmap[value]
            freq[count].append(value)

        print(freq)

        for i in range(len(freq) - 1, -1, -1):
            for val in freq[i]:
                if len(res) == k:
                    return res
                
                res.append(val)

        return res



        
        