class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #boyer moore algorithm

        candidate = nums[0]
        count = 1

        for value in nums[1:]:
            if value == candidate:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                candidate = value
                count = 1
        
        return candidate
        
        