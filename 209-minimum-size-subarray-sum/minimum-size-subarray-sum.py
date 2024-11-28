class Solution(object):
    def minSubArrayLen(self, target, nums):
        #   l = 0
        #   total = 0
        #   res = len(nums) + 1

        #   for r in range(len(nums)):
        #       total += nums[r]

        #       while(total >= target ):
        #           res = min( r - l + 1, res)
        #           total -= nums[l]
        #           l += 1

        #   if (res > len(nums)):
        #       return 0
        #   return res 

        # min_length = len(nums) + 1

        # start = 0
        # end = 0
        # current_sum = 0

        # while end <= len(nums):
        #     if current_sum >= target:
        #         if (end - start) < min_length:
        #             min_length = end - start
        #         current_sum -= nums[start]
        #         start += 1
        #     else:
        #         current_sum += nums[end]
        #         end += 1
        
        # if (min_length == len(nums) + 1):
        #     min_length = 0
        
        # return min_length

        min_len = len(nums) + 1
        start = 0
        current_sum = 0

        for end in range(1, len(nums) + 1):
            current_sum += nums[end - 1]
            while current_sum >= target:
                if (end - start) < min_len:
                    min_len = end - start
                
                current_sum -= nums[start]
                start += 1
        
        if min_len == len(nums) + 1:
            min_len = 0
        
        return min_len
            

                