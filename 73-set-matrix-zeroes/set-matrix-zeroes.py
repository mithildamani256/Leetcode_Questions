class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None. Modify matrix in-place.
        """
        if not matrix:
            return

        rows, cols = len(matrix), len(matrix[0])
        visit = set()

        # Step 1: Store the positions of all zeroes
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    visit.add((i, j))

        # Step 2: Set entire row and column to zero
        for i, j in visit:
            for h in range(rows):
                matrix[h][j] = 0  # Set column to zero
            for h in range(cols):
                matrix[i][h] = 0  # Set row to zero
 

                         



