class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        stack = []
        max_area = 0

        for i in range(len(heights)):
            current = heights[i] 
            until = i

            while stack and (current < stack[-1][1]):
                index, prev = stack.pop()
                prev_area = prev * (i - index)
                max_area = max(max_area, prev_area)

                until = index
        
            stack.append((until, current))

        while stack:
            i, h = stack.pop()

            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area