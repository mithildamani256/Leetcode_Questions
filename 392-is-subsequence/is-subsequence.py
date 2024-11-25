class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # i = 0
        # j = 0

        # if(s == ""):
        #     return True
        
        # while(j < len(t) and i < len(s)):
        #     if(s[i] == t[j]):
        #         i += 1
        #     if(i == len(s)):
        #         return True          
        #     j += 1
        
        # return False

        # current = -1

        # for i in range(len(s)):
        #     index = t.find(s[i])
        #     if index > current:
        #         current = index
        #     else:
        #         return False
        
        # return True

        x = -1
        flag = False

        for i in range(len(s)):
            flag = False
            val = s[i]

            for j in range(x + 1, len(t)):
                if t[j] == val:
                    x = j
                    flag = True
                    break
            
            if flag == False:
                return False
        
        return True
            
