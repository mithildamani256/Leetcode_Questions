class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        res = []
        path = []

        def dfs(index):
            if index == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[index])
            dfs(index + 1)
            path.pop()

            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            
            dfs(index+1)

        dfs(0)

        return res


# [1,2,2]

# 1,2,2
# 1,2,_
# 1,_,2
# 1,_,_
# _,2,2
# _,2,_
# _,_,2
# _,_,_


        