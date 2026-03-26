class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        symbols = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        special_strings = {"IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900}

        result = 0
        s_length = len(s)
        next_value = 0
        i = 0

        while i < s_length:
            symbol = s[i]
            value = symbols[symbol]

            if i + 1 < len(s):
                next_value = symbols[s[i+1]]
            else:
                result += value
                break
            
            if next_value <= value:
                result += value
                i += 1
            else:
                special_symbol = s[i] + s[i+1]
                value = special_strings[special_symbol]
                result += value
                i += 2

        return result

        




        
