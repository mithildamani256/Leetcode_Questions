class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagrams = {}
        result = []

        for word in strs:
            keyword = "".join(sorted(word))

            if keyword not in anagrams:
                anagrams[keyword] = []

            anagrams[keyword].append(word)

        for values in anagrams:
            result.append(anagrams[values])

        return result