class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 0 
        values = {}
        
        for i in range(len(nums)):
            if values.get(nums[i]) >= 1:
                continue
            else:
                nums[k] = nums[i] 
                values[nums[i]] = 1
                k += 1

        return k