class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hashmap = {}

        for i in range(len(nums)):
            value = hashmap.get(nums[i], 0)

            if value > 0:
                return True

            hashmap[nums[i]] = hashmap.get(nums[i] , 0) + 1

        return False
        