class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0])

        visit = set()

        def bfs(rotten):
            q = deque()
            annual = -1

            for t in rotten:
                i,j = t
                q.append((i,j))
                visit.add((i,j))

            directions = [(0,1), (1,0), (-1,0) , (0,-1)]

            while q:

                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dr, dc in directions:
                        cr, cc = r+dr, c +dc

                        if cr in range(rows) and cc in range(cols) and (cr,cc) not in visit and grid[cr][cc] == 1:
                            grid[cr][cc] = 2
                            visit.add((cr,cc))
                            q.append((cr,cc))

                annual += 1

            return max(annual,0)

        rotten = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append([r,c])

        time = bfs(rotten)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return time