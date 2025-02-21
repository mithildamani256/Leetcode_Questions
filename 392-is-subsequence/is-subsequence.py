class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        l = 0
        r = 0

        while r < len(t):
            if l >= len(s):
                return True
                
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                r += 1

        if l == len(s):
            return True

        return False