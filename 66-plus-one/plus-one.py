class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if not digits:
            return []

        if digits[-1] == 9:
            i = len(digits) - 1

            while digits[i] == 9:
                digits[i] = 0
                i -= 1

            if i >= 0:
                digits[i] += 1
            else:
                digits = [1] + digits

        else:
            digits[-1] += 1

        return digits
                
# digits -> [1,2,3]
# [1,2,4]

# [3,9]
# => [4,0]

# [2,3,9,9]
# => [2, 4,0,0]

# [9]
# [1,0]