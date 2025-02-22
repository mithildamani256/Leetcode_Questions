class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n

            maxSum = max(curSum, maxSum)

        return maxSum

