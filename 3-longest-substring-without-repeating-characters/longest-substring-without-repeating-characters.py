class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_length = 0
        substr = ""

        for right in range(len(s)):
            if s[right] not in substr:
                substr = substr + s[right]
                max_length = max(max_length, len(substr))
            else:
                while s[right] in substr:
                    substr = substr[1:]
                substr += s[right]


        return max_length
        