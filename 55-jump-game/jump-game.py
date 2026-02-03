class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        target = len(nums) - 1

        for i in range(len(nums) - 2, -1 , -1):
            if nums[i] + i >= target:
                target = i
        
        if target == 0:
            return True

        return False


        