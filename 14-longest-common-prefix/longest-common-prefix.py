class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # ans = ""
        # mini = len(strs[0])
        # min_index = 0
        # counter = -1

        # for i in range(len(strs)):
        #     if(len(strs[i]) < mini):
        #         mini = len(strs[i])
        #         min_index = i

        # smallest_elem = strs[min_index]

        # for val in smallest_elem:
        #     counter += 1
        #     for j in strs:
        #         if (val == j[counter]):
        #             continue
        #         else:
        #             return ans
            
        #     ans += val

        # return ans

        st = []
        first_str = strs[0]

        for i in range(len(first_str)):
            st.append(first_str[:i+1])

        st.reverse()
        st.append('')

        current_index = 0
        i = 0

        while i < len(strs):
            if st[current_index] == "":
                return ""

            if strs[i].startswith(st[current_index]):
                i += 1
            else:
                i = 0
                current_index += 1


        return st[current_index]



