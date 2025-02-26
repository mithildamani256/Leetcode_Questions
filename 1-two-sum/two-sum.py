class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}

        for i in range(len(nums)):
            value = target - nums[i]

            if value in hashmap:
                return [hashmap[value], i]

            hashmap[nums[i]] = i