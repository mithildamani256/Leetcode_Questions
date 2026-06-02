class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        path = []
        result = []

        def backtrack(i, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            if remaining < 0 or i >= len(candidates):
                return

            path.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i])
            path.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            backtrack(i + 1, remaining)

        backtrack(0, target)

        return result


# [1,1,6]
# target is 8

# u include 1 run it ahain -> include 1 run it again -> include 6 run it again returns. 
# 
        