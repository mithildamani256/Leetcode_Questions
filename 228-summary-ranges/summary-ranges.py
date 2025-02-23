class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        visit = set()
        return_lst = []

        for num in nums:
            if num in visit:
                continue

            visit.add(num)
            current_set = set()
            current_set.add(num)
            value = num + 1

            while value in nums:
                current_set.add(value)
                visit.add(value)
                value += 1

            current = "{}->{}".format(num, value - 1) if num != value - 1 else "{}".format(num)

            return_lst.append(current)
        
        return return_lst

        