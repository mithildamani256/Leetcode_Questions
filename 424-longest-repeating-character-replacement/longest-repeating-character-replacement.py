class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if not s:
            return 0

        freq = {s[0] : 1}

        max_length = 1
        left = 0

        for right in range(1, len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            if (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length