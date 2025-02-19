class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        ones = ["","I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["" , "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands = ["", "M", "MM", "MMM"]

        thousand = num // 1000
        hundred = (num % 1000) // 100
        ten = (num % 100) // 10
        one = (num % 10)


        return thousands[thousand] + hundreds[hundred] + tens[ten] + ones[one]



        