class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        if not points:
            return 0
        
        points.sort(key = lambda x : x[0])
        arrows = 1
        start, end = points[0][0], points[0][1]

        for i in range(1, len(points)):
            new_start, new_end = points[i][0], points[i][1]

            if new_start <= end:
                start = max(start, new_start)
                end = min(end, new_end)
            else:
                arrows += 1
                start, end = new_start, new_end
        
        return arrows


# first step is to sort it in increasing order by xstart
#  [1,6] => arrow is needed, start is 1 and end is 6
#  [2,8] => this overlaps with [1,6] so no new arrow needed. but now i need to ensure that arrow is between [2,6]
#  [7,12] => it doesnt overlap with [2,6] so new arrow needed. arrow += 1 , start = 7, end = 12
#  [10,16] => no arrow needed 