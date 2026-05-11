class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s
            
        rows = [[] for _ in range(numRows)]
        row, step = 0, 1

        for char in s:
            rows[row].append(char)
            if row == 0:
                step = 1          # going down
            elif row == numRows - 1:
                step = -1         # going up
            row += step

        return "".join("".join(r) for r in rows)

        # output_list = []
        # string_counter = 0
        # column_counter = 0
        # flag = True

        # while flag and string_counter < len(s):
        #     output_list.append([])
        #     for _ in range(numRows):
        #         if string_counter < len(s):
        #             current_char = s[string_counter]
        #             output_list[column_counter].append(current_char)
        #             string_counter += 1
        #         else:
        #             flag = False
        #             break
        #     column_counter += 1

        #     if not flag:
        #         break
            
        #     output_list.append([])
        #     output_list[column_counter].append("")

        #     for _ in range(numRows - 1, 1, -1):
        #         if string_counter < len(s):
        #             current_char = s[string_counter]
        #             output_list[column_counter].append(current_char)
        #             string_counter += 1
        #         else:
        #             break
            
        #     output_list[column_counter].append("")
        #     output_list[column_counter].reverse()
        #     column_counter += 1

        # print(output_list)
        # output_string = []
        # for i in range(numRows):

        #     for column in output_list:
        #         if i < len(column) and column[i] != "":
        #             output_string.append(column[i])

        # return "".join(output_string)
                
            
# some kinf of loop that goes over the string left to right from 0 to numrows
# once we reach numrows, keep going left to right in the string but now from numrows - 1 to 1 

#  PAYPAL, numrows = 3, [[P,A, Y], [P], [A,L]]
#  P     A
#  A  P  L
#  Y 