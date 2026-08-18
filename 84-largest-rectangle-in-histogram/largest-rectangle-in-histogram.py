class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            until = i
            while stack and stack[-1][1] > height:
                index, last_height = stack.pop()
                max_area = max(max_area, (i - index) * last_height)

                until = index
            
            stack.append((until, height))

        for index, height in stack:
            area = (len(heights) - index) * height
            max_area = max(area, max_area)

        return max_area
        