class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        v = s.split()
        answer = ""

        for i in range(len(v) - 1, -1 , -1):
            answer += v[i]
            answer += " "

        answer = answer.rstrip()
        return answer



        