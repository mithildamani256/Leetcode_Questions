class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        cur_end = 0      # farthest index we can reach with current number of jumps
        farthest = 0     # farthest index we can reach by taking one more step within current range

        for i in range(n - 1):  # no need to jump from last index
            farthest = max(farthest, i + nums[i])

            # when we reach the end of the current jump range, we must "take" a jump
            if i == cur_end:
                jumps += 1
                cur_end = farthest
                if cur_end >= n - 1:
                    break

        return jumps
