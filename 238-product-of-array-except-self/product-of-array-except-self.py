class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prefix_prod = []
        prefix = 1

        for i in range(len(nums)):
            prefix_prod.append(prefix)
            prefix = prefix * nums[i]
        
        postfix_prod = []
        postfix = 1

        for i in range(len(nums)):
            postfix_prod.append(postfix)
            postfix = postfix * nums[len(nums) - i - 1]

        result = []

        for i in range(len(nums)):
            cur = prefix_prod[i] * postfix_prod[len(nums) - i -1 ]
            result.append(cur)

        return result

        
        

            

        