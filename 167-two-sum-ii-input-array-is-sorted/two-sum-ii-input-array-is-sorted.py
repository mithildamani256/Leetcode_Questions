class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # l = 0
        # h = len(numbers) - 1

        # while(l < h):
        #     total = numbers[l] + numbers[h]
        #     if( total == target):
        #         return [l + 1, h + 1]
        #     elif ( total > target):
        #         h -= 1
        #     else:
        #         l += 1
        
        L = []

        i = 0
        j = len(numbers) - 1

        while i < j:
            current_sum = numbers[i] + numbers[j]

            if current_sum > target:
                j -= 1
            elif current_sum < target:
                i += 1
            else:
                L.append(i + 1)
                L.append(j+ 1)
                break
        
        return L
