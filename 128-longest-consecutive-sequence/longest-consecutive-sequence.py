class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        nums_set = set(nums)

        max_length = 0


        for val in nums_set:
            if val - 1 in nums_set:
                continue

            length = 0
            current_value = val

            while current_value in nums_set:
                current_value += 1
                length += 1
            
            max_length = max(max_length, length)

        return max_length