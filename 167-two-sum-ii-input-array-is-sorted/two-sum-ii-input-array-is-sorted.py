class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(numbers) - 1

        while True:
            current_sum = numbers[i] + numbers[j]
            if current_sum == target:
                return [i + 1,j + 1]
            
            elif current_sum > target:
                j -= 1
            
            else:
                i += 1
        
        return
        