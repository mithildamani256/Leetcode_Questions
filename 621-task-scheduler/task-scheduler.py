class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        task_dict = {}
        heap = []
        queue = deque()

        for task in tasks:
            task_dict[task] = task_dict.get(task, 0) + 1

        for freq in task_dict.values():
            heapq.heappush(heap, -freq)

        time = 0

        while heap or queue:
            time += 1

            if heap:
                current_freq = heapq.heappop(heap) + 1
                if current_freq:
                    queue.append((current_freq, time + n))

            if queue and queue[0][1] <= time:
                freq, _ = queue.popleft()
                heapq.heappush(heap, freq)

        return time


# use a max heap to determine which is the most frequent currently but also need to keep track of what cant be done right now

# tasks = ["A","C","A","B","D","B"], n = 1

# heap => {-2,-2,-1,-1}, queue = []

# -2 => -1
# time = 1

# heap => {-2,-1,-1}, queue = [(-1, 2)]
# heap => {-1,-1, -1}, queue = [(-1,3)]
