class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        first_half_nums = nums[:len(nums) - k]
        second_half_nums = nums[len(nums) - k : ]


        nums[:] = second_half_nums + first_half_nums