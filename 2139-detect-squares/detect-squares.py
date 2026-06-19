class DetectSquares(object):

    def __init__(self):
        self.ptscount = {}

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.ptscount[tuple(point)] = self.ptscount.get(tuple(point), 0) + 1

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """

        res = 0
        px, py = point[0], point[1]

        for x,y in (self.ptscount.keys()):
            if (abs(px - x) != abs(py - y)) or x == px or y == py:
                continue
            
            if ((x,py) in self.ptscount) and ((px,y) in self.ptscount):
                res += self.ptscount[(x, y)] * self.ptscount[(x,py)] * self.ptscount[(px,y)]
        
        return res
                 


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)