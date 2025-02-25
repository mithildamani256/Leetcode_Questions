class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r-l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]
        