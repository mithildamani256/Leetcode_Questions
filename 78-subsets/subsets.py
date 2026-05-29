class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        path = []

        nums_dict = {}

        for i, value in enumerate(nums):
            nums_dict[i] = value

        def dfs(index):
            if index == len(nums):
                result.append(path[:])
                return
            
            current_value = nums_dict[index]

            path.append(current_value)
            dfs(index + 1)
            path.pop()

            dfs(index + 1)
        
        dfs(0)

        return result



# if u have say nums = [1,2]

# 
        