class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        substr = ""

        for i in range(len(strs[0])):
            compare_char = strs[0][i]

            for word in strs[1:]:
                if i >= len(word) or compare_char != word[i]:
                    return substr
            substr += compare_char

        return substr

# for i in len(strs[0]):
#     compare_char = strs[i]
#     for word in strs[1:]:
        #   if compare_char is not equal to word[i]:
            # return substr

        # substr = substr + compare_char

# return substr

# strs = ["flower","flow","flight"]

