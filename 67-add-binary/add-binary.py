class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a_length = len(a) - 1
        b_length = len(b) - 1
        carry = 0
        result = ""

        while a_length >= 0 or b_length >= 0:
            if a_length >= 0:
                cur_a = int(a[a_length])
            else:
                cur_a = 0
            if b_length >= 0:
                cur_b = int(b[b_length])
            else:
                cur_b = 0

            value = cur_a + cur_b + carry

            carry = value // 2

            result += str(value % 2)

            a_length -= 1
            b_length -= 1
        
        if carry:
            result += str(carry)
        return result[::-1]
