class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort()
        
        res = 0
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]:
            if prevEnd > start:
                res += 1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end

        return res
