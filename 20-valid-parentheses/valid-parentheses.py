class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        brackets = {"}" : "{", ")" : "(", "]": "["}

        stack = []

        for value in s:
            if value not in brackets:
                stack.append(value)

            else:
                if not stack:
                    return False 
                    
                opener = stack.pop()
                if opener != brackets[value]:
                    return False
        
        if not stack:
            return True
        return False