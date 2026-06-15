class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for i in range(len(nums) + 1):
            res = res ^ i

        for value in nums:
            res = res ^ value

        return res
        