# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
        
#         res = []
#         freq= {}
#         left = 0

#         for i in range(k):
#             freq[nums[i]] = freq.get(nums[i], 0) + 1
        
#         res.append(max(freq))

#         for right in range(k, len(nums)):
#             freq[nums[right]] = freq.get(nums[right], 0) + 1
#             freq[nums[left]] -= 1
            
#             if freq[nums[left]] == 0:
#                 del freq[nums[left]]
#             left += 1
#             res.append(max(freq))

#         return res

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        dq = deque()   # stores indices
        res = []

        # BUILD FIRST WINDOW
        for i in range(k):

            # remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

        # max of first window
        res.append(nums[dq[0]])

        left = 0

        # SLIDE WINDOW
        for right in range(k, len(nums)):

            left += 1

            # # remove expired index
            if dq and dq[0] < left:
                dq.popleft()

            # remove smaller elements
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            # front of deque is maximum
            res.append(nums[dq[0]])

        return res