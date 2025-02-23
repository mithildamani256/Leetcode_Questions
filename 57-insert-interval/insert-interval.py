class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        intervals.append(newInterval)

        intervals = sorted(intervals, key = lambda x: x[0])
        output = [intervals[0]]

        for start,end in intervals[1:]:
            max_end = output[-1][1]

            if max_end >= start:
                output[-1][1] = max(max_end, end)

            else:
                output.append([start, end])

        return output