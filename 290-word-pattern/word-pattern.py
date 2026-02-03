class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        lst = s.split()

        if len(pattern) != len(lst):
            return False

        hashmap_pattern = {}
        hashmap_s = {}
        
        for i in range(len(lst)):
            a, b = lst[i], pattern[i]

            if a in hashmap_s:
                if hashmap_s[a] != b:
                    return False
            else:
                hashmap_s[a] = b

            if b in hashmap_pattern:
                if hashmap_pattern[b] != a:
                    return False
            else:
                hashmap_pattern[b] = a

        return True