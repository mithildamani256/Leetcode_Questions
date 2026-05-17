class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key = lambda x : x[0])

        last_start, last_end = intervals[0][0], intervals[0][1]

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i][0], intervals[i][1]

            if cur_start <= last_end:
                end = max(cur_end, last_end)
                result[-1] = [last_start, end]

            else:
                result.append(intervals[i])

            last_start = result[-1][0]
            last_end = result[-1][1]

        return result

        
# 1         ->          13
#   2 -> 6
#            8 - > 10
