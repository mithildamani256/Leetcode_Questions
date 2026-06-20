class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        if sum(gas) < sum(cost):
            return -1

        start = 0
        i = 0

        while i < len(gas):
            total = 0
            start = i
            
            while total + gas[i] >= cost[i]:
                if i == len(gas) - 1:
                    return start
                total = total + gas[i] - cost[i]

                i += 1
            
            i += 1
            

        return -1