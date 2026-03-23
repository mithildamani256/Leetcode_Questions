class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0:
            return []

        result = [1] * len(nums)

        prod = 1

        for i in range(len(nums)):
            result[i] = result[i] * prod
            prod = prod * nums[i]

        prod = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * prod
            prod = prod * nums[i]

        return result

        