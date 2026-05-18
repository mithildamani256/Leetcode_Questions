class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if not nums:
            return []

        res = []

        cur_start, cur_end = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] - 1 == cur_end:
                cur_end = nums[i]
            else:
                if cur_start == cur_end:
                    s = str(cur_start)
                    res.append(s)
                else:
                    res.append(str(cur_start) + "->" + str(cur_end))

                cur_start = nums[i]
                cur_end = nums[i]
        
        if cur_start == cur_end:
            s = str(cur_start)
            res.append(s)
        else:
            res.append(str(cur_start) + "->" + str(cur_end))

        return res
        
# [0,2,3,4,6,8,9]
#  cur_start = 0
#  cur_end = 0
#  for i in range(1, len(nums)):
#          if nums[i] - 1 == cur_end:
                    # cur_end = nums[i]
            # else:
                    # res.append(cur_start->cur_end)
                    # cur_start, cur_end = nums[i]
#  cur_end 