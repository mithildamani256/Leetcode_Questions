class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # prefix = []
        # prefix_total = 1

        # for val in nums:
        #     prefix_total = prefix_total * val
        #     prefix.append(prefix_total)
        
        # nums_rev = nums[::-1]
        # postfix_total = 1

        # postfix = []

        # for val in nums_rev:
        #     postfix_total = postfix_total * val
        #     postfix.append(postfix_total)
        
        # postfix.reverse()


        # answer = []
        # product_val = 1

        # for i in range(len(postfix)):
        #     if(i-1 < 0 and i + 1 >= len(nums)):
        #         answer.append(nums[i])
        #     elif (i - 1 < 0):
        #         product_val = postfix[i+1]
        #     elif(i + 1 >= len(nums)):
        #         product_val = prefix[i-1]
        #     else:
        #         product_val = prefix[i - 1] * postfix[i+1]

        #     answer.append(product_val)

        # return answer

        arr1 = []
        prefix_val = 1
        postfix_val = 1
        arr2 = []

        answer = []

        for i in range(len(nums)):
            arr1.insert(i, prefix_val)

            prefix_val *= nums[i]

        nums.reverse()

        for i in range(len(nums)):
            arr2.insert(i, postfix_val)

            postfix_val *= nums[i]

        arr2.reverse()

        for i in range(len(nums)):
            value = arr1[i] * arr2[i]
            answer.insert(i, value)

        return answer
            
        