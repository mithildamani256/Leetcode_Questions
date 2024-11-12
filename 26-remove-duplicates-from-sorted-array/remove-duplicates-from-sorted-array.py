class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # index = 0

        # for i in range(len(nums)):
        #     val = nums[i]
        #     if(val not in nums[i+1:]):
        #         nums[index] = val
        #         index = index + 1

        
        # return index

        k = 0
        j = 0

        while j < len(nums):
            if nums[j] not in nums[j+1:]:
                j = j + 1
                k = k + 1
            else:
                nums.pop(j)
        

        return k