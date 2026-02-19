class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort(key = lambda x: x[0])

        current = intervals[0]
        overlapping = 0

        for interval in intervals[1:]:
            start, end = interval

            if start < current[1]:
                overlapping += 1
                if end < current[1]:
                    current = interval
            else:
                current = interval

        return overlapping