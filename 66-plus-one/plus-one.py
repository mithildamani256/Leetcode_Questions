class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if not digits:
            return []

        if digits[-1] != 9:
            digits[-1] += 1

            return digits
        
        counter = len(digits) - 1

        while digits[counter] == 9:
            digits[counter] = 0
            counter -= 1
        
        if counter >= 0:
            digits[counter] += 1
            return digits
        
        else:
            return [1] + digits

# 130-138 -> + 1 on least significant
# 139 -> 140
# 199 -> 200
# 9 -> 10
# 
        