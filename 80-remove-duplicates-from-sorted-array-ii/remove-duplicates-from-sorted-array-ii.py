class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 2:
            return len(nums) 

        hashmap = {}

        for i in range(2):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1

        k = 2
        
        for i in range(2, len(nums)):
            value = hashmap.get(nums[i], 0)

            if value <= 1:
                nums[k] = nums[i]
                k += 1
            
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1


        return k

        