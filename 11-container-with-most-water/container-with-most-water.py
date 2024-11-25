class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i = 0
        j = len(height) - 1

        var_area = 0
        max_area = 0
        h = 0

        while j > i:
            if height[i] > height[j]:
                var_area = ( j - i ) * height[j]
                if var_area > max_area:
                    max_area = var_area
                j -= 1
            else:
                var_area = ( j - i ) * height[i]
                if var_area > max_area:
                    max_area = var_area
                i += 1           

        return max_area
    #     middle = len(height) // 2

    #     if len(height) == 1:
    #         return height[0]

    #     val1 = self.maxArea(height[:middle])
    #     val2 = self.maxArea(height[middle:])
    #     val3 = self.crossMax(height, middle)

    #     return max(val1, val2, val3)

    # def crossMax(self, A, middle):
    #     i = middle - 1
    #     j = middle

    #     var_area = 0
    #     max_area = 0
    #     height = max(A[i], A[j])

    #     while i >= 0 or j < len(A):
    #         if i < 0:
    #             height = min(height, A[j])
    #             var_area = (j - i) * height
    #             if var_area > max_area:
    #                 max_area = var_area
    #                 j += 1
    #         elif j >= len(A):
    #             height = min(height, A[i])
    #             var_area = (j - i) * height
    #             if var_area > max_area:
    #                 max_area = var_area
    #                 i -= 1
    #         elif A[i] > A[j]:
    #             height = min(height, A[i])
    #             var_area = (j - i) * height
    #             if var_area > max_area:
    #                 max_area = var_area
    #                 i -= 1
    #         else:
    #             height = min(height, A[j])
    #             var_area = (j - i) * height
    #             if var_area > max_area:
    #                 max_area = var_area
    #                 j += 1            

    #     return max_area   