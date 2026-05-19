class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []
        path_list = path.split("/")

        print(path_list)

        for i in range(len(path_list)):
            value = path_list[i]

            if value == "..":
                if stack:
                    stack.pop()
            elif value == "." or value == "":
                continue
            else:
                stack.append(value)

        return "/" + "/".join(stack)








        

        # cur = ""
        # i = 0

        # while i < len(path):
        #     value = path[i]

        #     if value == "/":
        #         i += 1
        #         continue
            
        #     elif value == ".":
        #         while i + 1 < len(path) and path[i+1] == ".":
        #             cur += "."
        #             i += 1

        #         if cur == "..":
        #             if stack:
        #                 stack.pop()
        #         elif cur == ".":
        #             continue
        #         else:
        #             stack.append(cur)
                
        #         cur = ""

        #     else:
        #         stack.append(value)

        #     i += 1

        # print(stack)




#  1st index to the end in path:
#  cur = ""
#  whhile i < len(path) : 
      # if value == "/":
            # continue
        
        # if value == ".":
            # if i + 1 < len(path) and path[i+1] == ".":
                # cur += "."
            # check value of cur , based on that pop from stack or add to stack or leave

        # else:
            #  stack.append(value)