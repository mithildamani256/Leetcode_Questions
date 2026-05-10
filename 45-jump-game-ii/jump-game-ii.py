class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        left = 0
        right = 0

        while len(nums) - 1 > right:
            right_boundary = 0

            for i in range(left, right + 1):
                boundary = i + nums[i]
                right_boundary = max(right_boundary, boundary)
            
            left = right + 1
            right = right_boundary
            counter += 1
        
        return counter

# {2,3,0,1,4}
# left 0, right 1 => left = 1, right = 3