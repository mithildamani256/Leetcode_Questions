class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        seen = []

        while n != 1:
            if n in seen:
                return False

            seen.append(n)

            n = sum(int(digit) ** 2 for digit in str(n))

        
        return True
