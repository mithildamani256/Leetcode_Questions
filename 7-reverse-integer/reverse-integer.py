import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        MIN = -2147483648  # -2^31
        MAX = 2147483647   #  2^31 - 1

        # FIX 1: Calculate boundaries using truncation (towards zero)
        # instead of Python's floor operators.
        MAX_DIV = int(MAX / 10)       #  214748364

        MAX_MOD = MAX % 10            #  7
        
        MIN_DIV = int(float(MIN) / 10)    # -214748364

        MIN_MOD = int(math.fmod(MIN, 10))   # -8
        
        res = 0
        while x:
            digit = int(math.fmod(x, 10))

            x = int(float(x) / 10)

            # if x < 0:
            #     x = -int(abs(x) // 10)  
            # else:
            #     x = int(x / 10)

            # Positive overflow check
            if (res > MAX_DIV or 
                (res == MAX_DIV and digit >= MAX_MOD)):
                return 0
                
            # FIX 2: Used the corrected MIN truncation boundaries here
            if (res < MIN_DIV or 
                (res == MIN_DIV and digit <= MIN_MOD)):
                return 0
                
            res = (res * 10) + digit

        return res