class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        zero_row_value = False
        zero_col_value = False

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                zero_col_value = True

                break

        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                zero_row_value = True

                break
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if zero_col_value:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if zero_row_value:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        return
        




#  rows = [false, false, false, ....]
#  cols = [false, false, false, false]

#  go ovr the matrix:
#    at each step, if char is 1, just update rows[i] and cols[j] to be true

#  for row in rows:
#       matrix[row] = [0 for _ in range(cols)]
#  for col in cols:
#       for r in range(len(rows)):
#           matrix[r][col] = 0