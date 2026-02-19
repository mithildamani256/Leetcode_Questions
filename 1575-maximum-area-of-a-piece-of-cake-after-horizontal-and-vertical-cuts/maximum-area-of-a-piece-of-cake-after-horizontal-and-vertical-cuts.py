class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """

        max_height = 0

        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        horizontalCuts.sort()

        max_width = 0

        verticalCuts.insert(0, 0)
        verticalCuts.append(w)
        verticalCuts.sort()

        for i in range(1, len(horizontalCuts)):
            max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i - 1])
        for i in range(1, len(verticalCuts)):
            max_width = max(max_width, verticalCuts[i] - verticalCuts[i - 1])

        max_area = max_height * max_width

        return max_area % (10**9 + 7)