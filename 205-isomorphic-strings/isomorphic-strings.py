class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if(len(s) != len(t)):
            return False

        replace = {}
        
        for i in range(len(s)):
            if (s[i] not in replace):
                replace[s[i]] = t[i]
            
            else:
                if (replace[s[i]] != t[i]):
                    return False

        replace = {}

        for i in range(len(t)):
            if (t[i] not in replace):
                replace[t[i]] = s[i]
            
            else:
                if (replace[t[i]] != s[i]):
                    return False
        
        return True   