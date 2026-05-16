class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        neighbours = [(-1,-1), (-1,0), (0,-1), (1,1), (0,1), (1,0), (1,-1), (-1,1)]

        # 1-> 0 represented by 2
        # 0 -> 1 represented by -2

        translations = {2:1, -2:0, 1:1, 0:0}

        for i in range((rows)):
            for j in range((cols)):
                current_value = board[i][j]
                output = 0
                for r,c in neighbours:
                    old_value = 0
                    if 0 <= i + r < rows and 0 <= j + c < cols:
                        cell = board[i + r][j + c]
                        old_value = translations[cell]

                    if old_value == 1:
                        output += 1
                
                if current_value == 1:
                    if output < 2:
                        board[i][j] = 2
                    elif output > 3:
                        board[i][j] = 2
                    else:
                        board[i][j] = 1
                
                else:
                    if output == 3:
                        board[i][j] = -2
                    else:
                        board[i][j] = 0

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -2:
                    board[i][j] = 1
                

        return




        