class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # n = []
        # p = []
        # z = []
        # res = []

        # for val in nums:
        #     if(val > 0):
        #         p.append(val)
        #     elif(val < 0):
        #         n.append(val)
        #     else:
        #         z.append(val)

        # N = set(n)
        # P = set(p)

        # if(len(z) >= 3):
        #     res.append([0,0,0])

        # if(len(z) > 0):
        #     for val in P:
        #         neg_val = -1 * val
        #         if(neg_val in N):
        #             res.append([neg_val, 0, val])
        
        # for i in range(len(n)):
        #     for j in range(i + 1, len(n)):
        #         val = -1 * (n[i] + n[j])
        #         if(val in P):
        #             if(n[j] > n[i]):
        #                 res.append([n[i], n[j], val])
        #             else:
        #                 res.append([n[j], n[i], val])
    
        # for i in range(len(p)):
        #     for j in range(i +1, len(p)):
        #         val = -1 * (p[i] + p[j])
        #         if(val in N):
        #             if(p[j] > p[i]):
        #                 res.append([val, p[i], p[j]])      
        #             else:
        #                 res.append([val, p[j], p[i]])      
        

        # resp = []
        # [resp.append(x) for x in res if x not in resp]
        # return resp

        # L = []
        # nums.sort()

        # for i in range(len(nums)):
        #     new_target = 0 - nums[i]

        #     a = 0
        #     b = len(nums) - 1

        #     while b > a:
        #         if a == i:
        #             a += 1
        #         if b == i:
        #             b -= 1

        #         if nums[b] + nums[a] > new_target:
        #             b -= 1
        #         elif nums[b] + nums[a] < new_target:
        #             a += 1
        #         else:
        #             L.append([i, a, b])

        
        # return L

        nums.sort()
        res = []

        for i, a in enumerate(nums):
            target = -a
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res

            
        
