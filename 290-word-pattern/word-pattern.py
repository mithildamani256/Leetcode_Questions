class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()

        if len(pattern) != len(s):
            return False
        
        values = {}

        for i in range(len(pattern)):
            if pattern[i] in values:
                if values[pattern[i]] != s[i]:
                    return False
            else:
                values[pattern[i]] = s[i]

        values = {}

        for i in range(len(s)):
            if s[i] in values:
                if values[s[i]] != pattern[i]:
                    return False
            else:
                values[s[i]] = pattern[i]

        
        return True
