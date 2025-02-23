class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        visit = set()

        for i in range(len(nums)):
            visit.add(nums[i])

        for i in range(0, n + 1):
            if i not in visit:
                return i
        