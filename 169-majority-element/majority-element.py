class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        values = {}

        for j in range(len(nums)):
            values[nums[j]] = 1 + values.get(nums[j], 0) 

            if values[nums[j]] > len(nums) / 2:
                return nums[j]
        