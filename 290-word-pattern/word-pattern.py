class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        lst = s.split()
        check = {}

        if (len(lst) != len(pattern)):
            return False

        for i, val in enumerate(pattern):
            if (val not in check):
                check[val] = lst[i]
            else:
                if (check[val] != lst[i]):
                    return False
        check = {}

        for i, val in enumerate(lst):
            if (val not in check):
                check[val] = pattern[i]
            else:
                if (check[val] != pattern[i]):
                    return False


        return True


        