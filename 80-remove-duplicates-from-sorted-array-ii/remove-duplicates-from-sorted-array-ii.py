class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # index = 1
        # count = 1
        # val = nums[0]

        # for i in range(1,len(nums)):
        #     if(val == nums[i]):
        #         count += 1

        #         if(count <= 2):
        #             nums[index] = val
        #             index += 1
        #     else:
        #         nums[index] = nums[i]
        #         count = 1
        #         val = nums[index]
        #         index += 1

        
        # return index 

        count = 1
        replace = 1

        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[replace] = nums[i]
                count = 1
                replace += 1
            else:
                count += 1
                if count <= 2:
                    nums[replace] = nums[i]
                    replace += 1

        return replace 
        