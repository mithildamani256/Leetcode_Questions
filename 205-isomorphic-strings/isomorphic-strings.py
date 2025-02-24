class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        hashmap = {}
        i = 0

        for char_s in s:
            char_t = t[i]
            if char_s in hashmap:
                val = hashmap[char_s]

                if val != char_t:
                    return False
            else:
                hashmap[char_s] = char_t

            i += 1

        hashmap = {}
        i = 0

        for char_t in t:
            char_s = s[i]
            if char_t in hashmap:
                val = hashmap[char_t]

                if val != char_s:
                    return False
            else:
                hashmap[char_t] = char_s

            i += 1


        return True

        