class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # k = k % len(nums)


        
        # for _ in range(k):
        #     val = nums.pop(-1)
        #     nums.insert(0, val)

        n = len(nums)
        k %= n 
        nums.reverse()
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])
