class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if (len(s) != len(t)):
            return False
        
        res = {}

        for val in s:
            if(val not in res):
                res[val] = 1
            else:
                res[val] += 1
        
        for val in t:
            if (val not in res):
                return False
            else:
                if (res[val] == 0):
                    return False
                else:
                    res[val] -= 1
        
        return True
        