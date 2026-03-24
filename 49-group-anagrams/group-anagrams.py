class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        result = []

        hashmap = {}

        for value in strs:
            keyword = "".join(sorted(value))

            if keyword in hashmap:
                hashmap[keyword].append(value)
            else:
                hashmap[keyword] = [value]

        for keyword in hashmap:
            result.append(hashmap[keyword])

        return result        