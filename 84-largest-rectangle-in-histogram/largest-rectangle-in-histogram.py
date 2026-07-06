class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        if not heights:
            return 0

        max_area = 0
        
        stack = []

        stack.append((heights[0],0))

        for i in range(1, len(heights)):
            current_height = heights[i]
            until = i

            while stack and  stack[-1][0] > current_height:
                prev, index = stack.pop()
                max_area = max(max_area, (i - index) * prev)
                until = index
            
            stack.append((current_height, until))


        while stack:
            height, start = stack.pop()

            max_area = max(max_area, (len(heights) - start) * height)

        return max_area
        




# [2,1,5,6,2,3]

# =>

# stack - [(2,0)] (monotonically increasing stack)
# when you see 1, you pop form the stack to get 2. 
# the area u can get from 2 is (index of 1 - whatever 2 had on stack) * 2

# stack = [(1,0)]
# stack = [1,5,6]
# 2 
# pop 6. calculate the area -> ()
# pop 5, calculate the area
# but now when adding 2, u need to add (2,2)
# u need to add the index of where you can start to take area including this element
        