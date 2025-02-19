class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0

        while val in nums:
            nums.remove(val)
            k += 1

        for i in range(k):
            nums.append(val)

        return len(nums) - k


