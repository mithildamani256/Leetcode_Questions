class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals = sorted(intervals, key = lambda x : x[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:
            max_end = output[-1][1]

            if max_end >= start:
                output[-1][1] = max(max_end, end)

            else:
                output.append([start, end])

        
        return output
    
        

            

        