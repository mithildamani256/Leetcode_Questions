class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])
        visit = set()

        def bfs(r,c):
            touches_border = False
            region = []
            q = deque()

            q.append((r,c))
            visit.add((r,c))
            region.append((r,c))
            
            directions = [(0,1), (1,0), (0,-1), (-1,0)]

            while q:
                r,c = q.popleft()

                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    touches_border = True

                for dr,dc in directions:
                    cur_row, cur_col = r + dr, c + dc

                    if cur_row in range(rows) and cur_col in range(cols) and board[cur_row][cur_col] == "O" and (cur_row,cur_col) not in visit:
                        region.append((cur_row,cur_col))
                        visit.add((cur_row,cur_col))
                        q.append((cur_row, cur_col))

            return region, touches_border

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visit:
                    regions, touch_border = bfs(r,c)

                    if not touch_border:
                        for row, col in regions:
                            board[row][col] = "X"

        return 
        