class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i = 0
        j = len(height) - 1
        max_area = 0

        while i < j:
            current_height = min(height[i], height[j])
            current_area = (current_height) * (j - i)

            max_area = max(max_area, current_area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
        
#  two pointers i = 0, j = len(height) - 1
# calculate height = min(height[i], height[j]) * (j - i)
# update max_height = max(maxheight, height)
#  if i < j:
    #     i += 1
    # else:
    #     j -= 1