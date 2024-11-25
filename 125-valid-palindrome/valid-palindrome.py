class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # my_str = ""

        # for val in s:
        #     if(val.isalnum()):
        #         my_str += val.lower()

        # compare_str = my_str[::-1]

        # if(compare_str == my_str):
        #     return True
    
        # return False

        ans = ""

        for val in s:
            if (val.isalnum()):
                ans += val

        ans = ans.lower()
        
        i = 0
        j = len(ans) - 1

        while j >= i:
            if ans[i] != ans[j]:
                return False
            i += 1
            j -= 1

        return True
