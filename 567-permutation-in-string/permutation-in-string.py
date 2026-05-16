class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2):
            return False

        counter = Counter(s1)
        window = {}
        left = 0

        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1
        
        if window == counter:
            return True
        
        for right in range(len(s1), len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]
                
            if window == counter:
                return True
        
            left += 1
        
        return False

# eadeabc
# eab
        