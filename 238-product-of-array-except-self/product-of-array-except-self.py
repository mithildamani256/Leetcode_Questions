class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = [1] * len(nums)
        prefix = 1

        for i in range(0, len(nums) - 1):
            prefix = prefix * nums[i]
            output[i+1] = prefix
        
        suffix = 1

        for i in range(len(nums) -1 , 0, -1):
            suffix = suffix * nums[i]
            output[i - 1] *= suffix

        return output
         
# {3,4,5,6}
# prefix => {1,3,12, 60}
# suffix => {}