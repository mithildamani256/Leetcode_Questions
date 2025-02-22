class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0
        
        rows, cols = len(grid) , len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque([(r,c)])
            q.append((r,c))
            visit.add((r,c))

            while q:
                r, c = q.popleft()
                directions = [[1,0], [0,1], [0,-1], [-1,0]]

                for dr, dc in directions:
                    if (r+dr) in range(rows) and (c + dc) in range(cols) and (r+dr, c+dc) not in visit and grid[r+dr][c+dc] == "1":
                        visit.add((r+dr, c+dc))
                        q.append((r+dr, c+dc))

            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands