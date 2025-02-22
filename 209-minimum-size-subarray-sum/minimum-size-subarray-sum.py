class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        # left = 0
        # min_length = float('inf')
        # total = 0

        # for right in range(len(nums)):
        #     total += nums[right]
        #     if total >= target:
        #         min_length = min(min_length, right - left + 1)
        #         while total - nums[left] >= target:
        #             left += 1
        #             min_length = min(min_length, right - left + 1)
        #             total = total - nums[left]

        # if min_length == float('inf'):
        #     return 0

        # return min_length
        left = 0
        min_length = float('inf')
        total = 0

        for right in range(len(nums)):  # ✅ Expand window with `right`
            total += nums[right]

            while total >= target:  # ✅ Shrink window with `left`
                min_length = min(min_length, right - left + 1)
                total -= nums[left]  # ✅ Reduce window sum correctly
                left += 1  # ✅ Move left pointer forward

        return min_length if min_length != float('inf') else 0
        
        