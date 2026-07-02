class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # lst = s.split()

        # return len(lst[-1])

        i = 0

        while i < len(s):

            if s[i] == " ":
                i += 1
                continue

            length = 0

            while i < len(s) and s[i] != " ":
                length += 1
                i += 1

            i += 1

        return length


# "   fly me   to   the moon  "

# 
        