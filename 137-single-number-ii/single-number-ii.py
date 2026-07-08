class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0

        for i in range(32):
            count = 0
            for value in nums:
                bit = (value >> i) & 1

                if bit:
                    count += 1
                
            if count % 3 == 1:
                res = (1 << i) | res
        
        if res >= 2**31:
            res = res - 2**32
        return res
        