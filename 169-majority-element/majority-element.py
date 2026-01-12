class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        candidate = nums[0]
        count = 1

        for val in nums[1:]:
            if val != candidate:
                count -= 1
            else:
                count += 1
            
            if count == 0:
                count = 1
                candidate = val
            
        
        return candidate
        