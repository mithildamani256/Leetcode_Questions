class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        answer = ""

        for r in range(numRows):
            increment = (numRows - 1) * 2
            for j in range(r, len(s), increment):
                answer += s[j]

                if(r > 0  and r < numRows - 1 and j + increment - 2 * r < len(s)):
                    answer += s[j + increment - 2* r]

        
        return answer



        