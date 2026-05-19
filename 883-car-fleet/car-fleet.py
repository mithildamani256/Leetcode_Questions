class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        pairs = [(position[i], speed[i]) for i in range(len(position))]
        fleets = curtime = 0  # a car's position is always < than target at the start, so it's fine to start curtime at 0 (no fleet will be at target at time 0)
        
        for dist, spd in sorted(pairs, reverse=True):
            destination_time = float(target - dist) / spd
            if curtime < destination_time:
                fleets += 1
                curtime = destination_time

        return fleets