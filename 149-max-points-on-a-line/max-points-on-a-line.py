class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        res = 1

        for i in range(len(points)):
            p1 = points[i]
            count = {}

            for j in range(i+1, len(points)):
                p2 = points[j]

                if p2[0] == p1[0]:
                    slope = float('inf')
                else:
                    slope = float(p2[1] - p1[1]) / (p2[0] - p1[0])

                count[slope] = count.get(slope, 0) + 1

                res = max(res, count[slope] + 1)

        return res

                

        