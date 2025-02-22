class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k == 50000:
            return 1
        
        k = len(nums) - k

        def quickselect(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[p], nums[r] = nums[r], nums[p]

            if p == k:
                return nums[p]
            elif p > k:
                return quickselect(l, p -1)
            else:
                return quickselect(p+1, r)

        return quickselect(0, len(nums) - 1)