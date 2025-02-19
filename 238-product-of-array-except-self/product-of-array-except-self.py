class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        value = 1
        prefix = []
        postfix = []

        for i in range(len(nums)):
            prefix.append(value)

            value *= nums[i]

        nums.reverse()
        value = 1

        for i in range(len(nums)):
            postfix.append(value)

            value *= nums[i]

        postfix.reverse()


        for j in range(len(nums)):
            nums[j] = prefix[j] * postfix[j]


        return nums



