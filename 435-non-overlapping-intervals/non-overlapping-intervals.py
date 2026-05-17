class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort(key = lambda x : x[0])
        last_end = intervals[0][1]
        overlapping = 0

        for i in range(1, len(intervals)):
            if last_end > intervals[i][0]:
                last_end = min(intervals[i][1], last_end)
                overlapping += 1
            
            else:
                last_end = intervals[i][1]

        return overlapping
        
# sort by start date. then go over the intervals one at a time. 
#  for each interval if u think it is overlapping, keep the interval that ends first. 

#  [[1,2],[2,3],[3,4],[1,3]]

# => [[1,2],[1,3], [2,3],[3,4]]

#  last_end = 2
# [1,3] => last_end = 2
# [2,3] => last_end = 3
# [3,4] => overlapping not nupdated 
# return 1