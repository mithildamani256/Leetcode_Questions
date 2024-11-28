class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # for i in ransomNote:
        #     if i in magazine:
        #         val = magazine.index(i)
        #         magazine = magazine[:val] + magazine[val+1:]
        #     else:
        #         return False

        # return True            
        usable = {}

        for s in magazine:
            if (s in usable):
                usable[s] += 1
            else:
                usable[s] = 1
        
        for s in ransomNote:
            if (s not in usable):
                return False
            if (s in usable):
                if (usable[s] == 0):
                    return False
                else:
                    usable[s] -= 1
        

        return True
