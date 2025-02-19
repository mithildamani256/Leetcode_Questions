class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        longest_substring = ""

        for i in range(len(strs[0])):

            for j in range(len(strs)):
                if i >= len(strs[j]):
                    return longest_substring

                if strs[0][i] != strs[j][i]:
                    return longest_substring

            longest_substring += strs[0][i]
        

        return longest_substring