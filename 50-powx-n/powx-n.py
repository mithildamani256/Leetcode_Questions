import math

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n > 0:
            return math.pow(x,n)

        else:
            return math.pow(1/x, -n)

        