import math

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # compare = len(nums)/2
        # max_element = ""
        # max_number = 0

        # for i in range(len(nums)):
        #     val = nums[i]
        #     count = 1
        #     for j in range(i+1, len(nums)):
        #         if (val == nums[j]):
        #             count += 1

        #     if(count > compare):
        #         max_element = val
        #         max_number = count
        
        # return max_element

        # for i in range(len(nums)):
        #     candidate = nums[i]
        #     count = 1
        #     for j in range(i+1, len(nums)):
        #         if(candidate == nums[j]):
        #             count += 1
        #         else:
        #             count -= 1
        #     if(count > 0):
        #         return candidate
        # count = 0
        # candidate = 0
        
        # for num in nums:
        #     if count == 0:
        #         candidate = num
            
        #     if num == candidate:
        #         count += 1
        #     else:
        #         count -= 1
        
        # return candidate

        dict = {}
        count = math.floor(len(nums) / 2)

        for i in range(len(nums)):
            dict[nums[i]] = dict.get(nums[i], 0) + 1

            if dict[nums[i]] > count:
                return nums[i]
