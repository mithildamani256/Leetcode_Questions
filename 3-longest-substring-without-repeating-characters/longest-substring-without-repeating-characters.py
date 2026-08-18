class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = 0
        left = 0
        substring = set()

        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            
            substring.add(s[right])
            length = max(length, right - left + 1)
        
        return length
        