class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if k == 0:
            return nums
        
        k = k % len(nums)

        new_head = nums[len(nums)- k :]
        new_tail = nums[:len(nums) - k]
        nums[:] = new_head + new_tail

        # new_head = nums[len(nums)- k : ]
        # new_tail = nums[:len(nums)- k]

        # nums[:] = new_head + new_tail

        # return

        