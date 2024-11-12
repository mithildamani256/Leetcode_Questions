class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        replace = 1

        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[replace] = nums[i]
                replace += 1
        

        return replace