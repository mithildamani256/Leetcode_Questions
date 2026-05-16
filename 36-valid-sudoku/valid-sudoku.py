class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]

        boxes = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                character = board[i][j]

                if character == ".":
                    continue

                if character in rows[i]:
                    return False
                
                if character in cols[j]:
                    return False
                
                rows[i].append(character)
                cols[j].append(character)

                current_box = (i // 3) * 3 + (j // 3)

                if character in boxes[current_box]:
                    return False
                
                boxes[current_box].append(character)

        return True
