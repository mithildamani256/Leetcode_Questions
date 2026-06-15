class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        result = []
        
        for value in range(n+1):
            ones = 0
            while value:
                if value % 2 == 1:
                    ones += 1
                value = value // 2
        
            result.append(ones)

        return result