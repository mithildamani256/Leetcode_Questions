class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s_list = s.split()

        s_list.reverse()

        s = " ".join(s_list)

        return s
        