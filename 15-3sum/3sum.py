class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            target = -nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum > target:
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    new_triplet = [nums[i], nums[left], nums[right]]
                    result.append(new_triplet)

                    left += 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
            
        return result


#  we would have to sort the array O(nlogn)
#  go over the array one element at a time creating a new target value for rest of the array
#           for each index i , check whether it is not equal to i - 1
#  use a two pointer approach on the remaining elements. 
#  once u find an index range [i,j]
#  move forward until say nums[i] is not equal to nums[i + 1]