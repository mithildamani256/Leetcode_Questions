class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 0 or len(nums) == 1:
            return True

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

            if goal == 0:
                return True
        
        return False

# [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

# [2,3]
# [3,3,4]
# [3,4,4,5]
# 4,4,5,4,5