class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0
        r = len(nums) - 1
        res = 0

        while l <= r:
            m = l + (r-l)//2

            if nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m + 1
                res = m + 1
            else:
                res = m 
                break

        return res

            
            