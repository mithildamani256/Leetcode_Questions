class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                day, previous_temp = stack.pop()
                result[day] = i - day
            stack.append([i, temp])
        
        return (result)

# [73,74,75,71,69,72,76,73]
# stack = [[0,73]]

# result[0] = 