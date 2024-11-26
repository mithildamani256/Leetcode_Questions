class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # maxlen_substr = 0
        # max_substr = ""
        # substr = ""

        # for x in s:
        #     if x not in substr:
        #         substr += x
        #     else:
        #         if (len(substr) > maxlen_substr):
        #             maxlen_substr = len(substr)
        #             max_substr = substr
        #             substr = x
        
        # # print(max_substr)
        # return maxlen_substr

        # l = 0
        # x = ""
        # max_len = 0
        
        # for r in range(len(s)):
        #     if(s[r] in x):
        #         max_len = max(len(x), max_len)
        #         l += 1
        #         x = s[l:r]

        #     else:
        #         x += s[r]

        # return max_len

        if s == "":
            return 0

        longest_length = 1
        substring = s[0]
        longest_substring = s[0]

        start = 0

        for end in range(1, len(s)):
            if s[end] not in substring:
                substring = substring + s[end]
            else:
                start = s.find(s[end], start) + 1
                substring = s[start : end + 1]
            
            if (len(substring) > longest_length):
                longest_length = len(substring)
                longest_substring = substring
        
        return longest_length