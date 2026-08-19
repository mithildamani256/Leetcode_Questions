class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        max_area = 0

        visit = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            q = deque()
            
            visit.add((r,c))
            q.append((r,c))

            area = 1

            while q:
                row, col = q.popleft()

                directions = [(0,1), (1,0), (-1,0), (0,-1)]

                for dr, dc in directions:
                    cur_row, cur_col = dr +row, dc + col

                    if cur_row in range(rows) and cur_col in range(cols) and grid[cur_row][cur_col] == 1 and (cur_row, cur_col) not in visit:
                        area += 1
                        visit.add((cur_row, cur_col))
                        q.append((cur_row, cur_col))
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = bfs(r,c)
                    max_area = max(max_area, area)
        
        return max_area
        