class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        cur_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += num

            max_sum = max(max_sum, cur_sum)

        return max_sum

        