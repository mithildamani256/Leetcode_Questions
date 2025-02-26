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

            
        hashmap = {}

        for i in range(len(pattern)):
            if pattern[i] in hashmap:
                value = hashmap[pattern[i]]

                if value != s[i]:
                    return False

            else:
                hashmap[pattern[i]] = s[i]    


        hashmap = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                value = hashmap[s[i]]

                if value != pattern[i]:
                    return False

            else:
                hashmap[s[i]] = pattern[i]   

        return True 