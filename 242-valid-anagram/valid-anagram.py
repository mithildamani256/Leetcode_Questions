class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        old = {}

        for val in s:
            old[val] = old.get(val, 0) + 1

        for val in t:
            if old.get(val, 0) == 0:
                return False
            else:
                old[val] -= 1

        for val in old:
            if old[val] != 0:
                return False

        return True        