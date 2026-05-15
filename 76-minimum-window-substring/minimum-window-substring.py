class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        window = {}
        counter = Counter(t)
        left = 0

        have = 0
        required = len(counter)

        min_length = float('inf')
        min_substr = [-1,-1]

        for right in range(len(s)):

            window[s[right]] = window.get(s[right],0) + 1

            if window[s[right]] == counter[s[right]]:
                have += 1
            
            while have == required:

                if right - left + 1 < min_length:
                    min_length = min(min_length, right - left + 1)
                    min_substr = [left, right]

                window[s[left]] -= 1

                if s[left] in counter and window[s[left]] < counter[s[left]]:
                    have -= 1

                left += 1
            

        if min_length == float('inf'):
            return ""

        return s[min_substr[0]:min_substr[1] + 1]
                





        
# window = {}
# left = 0
# counter = Counter(t)
# have, required = have -> how many chars in t are satisfied, and required is just no of unique characters in t
# 