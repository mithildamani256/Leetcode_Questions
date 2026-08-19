class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c,last_height,visit):
            if (r,c) in visit or r not in range(rows) or c not in range(cols) or heights[r][c] < last_height:
                return
            
            visit.add((r,c))

            dfs(r+1, c , heights[r][c], visit)
            dfs(r-1, c , heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)

            return

        for r in range(rows):
            dfs(r,0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols-1], atl)
        
        for c in range(cols):
            dfs(0,c,heights[0][c], pac)
            dfs(rows - 1, c, heights[rows-1][c], atl)


        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

        
