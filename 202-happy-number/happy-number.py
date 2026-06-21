class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        hash_set = set()
        hash_set.add(n)

        while n != 1:
            new_n = 0

            for value in str(n):
                new_n += int(value) ** 2
            
            if new_n in hash_set:
                return False

            hash_set.add(new_n)

            n = new_n

        return True


        