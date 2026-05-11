class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        list_s = s.split()

        return " ".join(list_s[::-1])   