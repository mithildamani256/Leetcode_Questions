class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        values = {}

        for val in magazine:
            values[val] = values.get(val, 0) + 1

        for val in ransomNote:
            if values.get(val, 0) == 0:
                return False
            values[val] -= 1
    
        return True
        