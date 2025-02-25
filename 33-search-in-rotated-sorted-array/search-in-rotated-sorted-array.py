class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l , r = 0, len(nums) - 1

        while l < r:
            m = l + (r-l)//2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        min_index = l

        if nums[min_index] == target:
            return min_index

        if target <= nums[-1]:
            l, r = min_index + 1, len(nums) - 1
        else:
            l, r = 0, min_index - 1
        
        while l <= r:
            m = l + (r-l)//2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m -1
            else:
                l = m + 1

        return -1
        