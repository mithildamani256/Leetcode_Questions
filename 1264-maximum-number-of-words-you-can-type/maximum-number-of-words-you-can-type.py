class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """

        text_lst = text.split()
        result = 0

        for word in text_lst:
            broken = False
            for letter in brokenLetters:
                if letter in word:
                    broken = True
                    break

            if not broken:
                result += 1

        return result